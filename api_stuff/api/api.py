from fastapi import FastAPI, HTTPException, Request
import threading
import uvicorn
import hosts_holder
import httpx
import api_functions
import logs

app = FastAPI()


@app.get("/{path:path}")
async def query(path: str):
    host_id = api_functions.get_host_id_to_redirect()
    if host_id == -1:
        raise HTTPException(status_code=500, detail="The service fell in battle :(")

    hosts_holder.status_hosts[host_id]["count"] = hosts_holder.status_hosts[host_id].get("count") + 1
    url = f'{hosts_holder.status_hosts[host_id].get("host")}/{path}'

    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        hosts_holder.status_hosts[host_id]["count"] = hosts_holder.status_hosts[host_id].get("count") - 1
        return response.content, response.status_code


@app.post("/statistics")
async def statistics():
    return api_functions.statistics()


if __name__ == '__main__':
    logs.init_logger()
    api_functions.load_config_hosts()

    thread_health = threading.Thread(target=api_functions.check_health_server)
    thread_health.start()

    thread_logs = threading.Thread(target=api_functions.deamon_save_log)
    thread_logs.start()
    uvicorn.run(app, host='0.0.0.0', port=5000)
