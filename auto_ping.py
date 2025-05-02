import os
import statistics
from colorama import Fore, Style
import time

def ping_target(target):
    print(f"\n{Fore.YELLOW}Mulai ping ke {target}...\n{Style.RESET_ALL}")
    
    # Melakukan ping dan menyimpan waktu latensi
    latencies = []
    packets_sent = 0
    packets_received = 0

    for seq in range(1, 4):  # Lakukan 3 ping
        response = os.popen(f"ping -c 1 {target}").read()
        
        if "time=" in response:
            # Mengambil waktu dari output ping
            time_ms = response.split("time=")[-1].split(" ms")[0]
            latencies.append(float(time_ms))
            print(f"64 bytes from {target}: icmp_seq={seq} ttl=118 time={time_ms} ms")
            packets_sent += 1
            packets_received += 1
        else:
            print(f"{Fore.RED}{target} TIDAK DAPAT dijangkau ❌{Style.RESET_ALL}")
            packets_sent += 1  # Tetap hitung pengiriman paket meskipun gagal
            continue
    
        time.sleep(1)  # Jeda 1 detik antara ping
    
    # Menghitung packet loss
    packet_loss = (packets_sent - packets_received) / packets_sent * 100
    
    # Output hasil ping
    print(f"\n{Fore.CYAN}Ping selesai!{Style.RESET_ALL}")
    print(f"{Fore.GREEN}Paket terkirim: {packets_sent}, Paket diterima: {packets_received}{Style.RESET_ALL}")
    print(f"{Fore.RED}Packet loss: {packet_loss:.2f}%{Style.RESET_ALL}")
    
    return latencies

def show_loading():
    print(f"{Fore.YELLOW}Memproses hasil ping", end="")
    for _ in range(3):
        time.sleep(0.5)
        print(".", end="", flush=True)
    print()  # Newline after loading

def main():
    print(f"{Fore.CYAN}Network Ping Automation{Style.RESET_ALL}")
    target = input(f"{Fore.GREEN}Masukkan IP atau hostname untuk dicek (misal: 8.8.8.8): {Style.RESET_ALL}")
    
    latencies = ping_target(target)
    
    if latencies:
        show_loading()  # Menampilkan efek loading
        
        avg_latency = sum(latencies) / len(latencies)
        jitter = statistics.stdev(latencies) if len(latencies) > 1 else 0
        
        print(f"\n{Fore.BLUE}Hasil Ping ke {target}:{Style.RESET_ALL}")
        print(f"{Fore.GREEN}Latensi Rata-Rata: {avg_latency:.2f} ms{Style.RESET_ALL}")
        print(f"{Fore.GREEN}Jitter (Variansi): {jitter:.2f} ms{Style.RESET_ALL}")
        if jitter < 5:
            print(f"{Fore.GREEN}Jitter rendah, jaringan stabil!{Style.RESET_ALL}")
        else:
            print(f"{Fore.RED}Jitter tinggi, periksa koneksi jaringan!{Style.RESET_ALL}")

if __name__ == "__main__":
    main()
