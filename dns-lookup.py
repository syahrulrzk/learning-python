import socket

domains = ["google.com", "yahoo.com", "openai.com"]

for domain in domains:
    try:
        ip = socket.gethostbyname(domain)
        print(f"{domain} → {ip}")
    except socket.gaierror:
        print(f"Gagal resolve: {domain}")
