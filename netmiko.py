from netmiko import ConnectHandler

cisco_device = {
    'device_type': 'cisco_ios',
    'ip': '192.168.1.1',
    'username': 'admin',
    'password': 'admin123',
}

# Connect dan kirim perintah
connection = ConnectHandler(**cisco_device)
output = connection.send_command('show ip int brief')
print(output)

connection.disconnect()
