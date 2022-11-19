import threading
import requests


def spammer():
    for i in range(10000):
        yield requests.get(f'http://localhost:9010//')


arr_th = []
count_th = 80
for i in range(count_th):
    arr_th.append(threading.Thread(target=spammer))

for i in arr_th:
    i.start()
    print(f'run th: {i}')

for i in arr_th:
    i.join()
    print(f'end th: {i}')
