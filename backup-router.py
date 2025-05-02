from datetime import datetime

config_data = """
interface GigabitEthernet0/1
 description Link to ISP
 ip address 192.168.1.1 255.255.255.0
 no shutdown
"""

filename = f"backup_config_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
with open(filename, 'w') as f:
    f.write(config_data)

print(f"Konfigurasi berhasil disimpan ke {filename}")
