import socket

target = "google.com"
ports = [22, 80, 443]

print(f"Mengecek port pada {target}...\n")

for port in ports:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)
    
    result = sock.connect_ex((target, port))
    if result == 0:
        print(f"Port {port} TERBUKA ✅")
    else:
        print(f"Port {port} TERTUTUP ❌")
    sock.close()
