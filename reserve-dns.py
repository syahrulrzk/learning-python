import socket

ips = ["8.8.8.8", "1.1.1.1", "127.0.0.1"]

for ip in ips:
    try:
        host = socket.gethostbyaddr(ip)
        print(f"{ip} → {host[0]}")
    except socket.herror:
        print(f"{ip} → Tidak ditemukan nama host")
