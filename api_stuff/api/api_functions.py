from threading import Event
import logs
import hosts_holder
import http
import httpx
import json
import os


def check_health_server():
    while True:
        try:
            for i in range(len(hosts_holder.status_hosts)):
                url = f'{hosts_holder.status_hosts[i].get("host")}/health'
                try:
                    respons = httpx.post(url=url)
                    if respons.status_code == http.HTTPStatus.OK:
                        hosts_holder.status_hosts[i]["status"] = True
                    else:
                        hosts_holder.status_hosts[i]["status"] = False
                        hosts_holder.status_hosts[i]["count"] = 0
                except:
                    hosts_holder.status_hosts[i]["status"] = False
                    hosts_holder.status_hosts[i]["count"] = 0
        except Exception as e:
            logs.save_log_error(e)
        Event().wait(10)


def get_host_id_to_redirect():
    number_of_requests = None
    host_id = None
    for i in range(len(hosts_holder.status_hosts)):
        if hosts_holder.status_hosts[i].get("status"):
            if number_of_requests is None:
                number_of_requests = hosts_holder.status_hosts[i].get("count")
                host_id = i
            if hosts_holder.status_hosts[i].get("count") < number_of_requests:
                number_of_requests = hosts_holder.status_hosts[i].get("count")
                host_id = i
    if host_id is None:
        logs.save_log_critical("no live hosts")
        return -1
    return host_id


def load_config_hosts():
    try:
        with open('api/config_hosts.json', "r") as file_object:
            data = file_object.read()
            arr_host = json.loads(data)
            for item in arr_host:
                hosts_holder.status_hosts.append({
                    "host": item,
                    "count": 0,
                    "status": False
                })
    except Exception as e:
        logs.save_log_error(e)


def statistics():
    try:
        app_name = os.environ["APP"]
        if app_name:
            return {app_name: hosts_holder.status_hosts}
    except:
        return hosts_holder.status_hosts


def deamon_save_log():
    while True:
        st = statistics()
        logs.save_log_info(st)
        Event().wait(1)
