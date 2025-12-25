#!/usr/bin/env python3

import nmap
import re

ip_add_pattern = re.compile(r"^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$")
port_range_pattern = re.compile(r"([0-9]+)-([0-9]+)")

print(r"""
______            _     _____                                 
| ___ \          | |   /  ___|                                
| |_/ /__  _ __  | |_  \ `--.  ___ __ _ _ __  _ __   ___ _ __ 
|  __/ _ \| '__| | __|  `--. \/ __/ _` | '_ \| '_ \ / _ \ '__|
| | | (_) | |    | |_  /\__/ / (_| (_| | | | | | | |  __/ |   
\_|  \___/|_|     \__| \____/ \___\__,_|_| |_|_| |_|\___|_|   
""")

print("***********************")
print("*     PORT SCANNER    *")
print("***********************")

while True:
    ip_add_entered = input("\nEnter target IP address: ")
    if ip_add_pattern.search(ip_add_entered):
        break
    else:
        print("Invalid IP address.")

while True:
    port_range = input("Enter port range (e.g. 20-100): ")
    match = port_range_pattern.search(port_range.replace(" ", ""))
    if match:
        port_min = int(match.group(1))
        port_max = int(match.group(2))
        break
    else:
        print("Invalid port range.")

nm = nmap.PortScanner()

for port in range(port_min, port_max + 1):
    try:
        result = nm.scan(ip_add_entered, str(port))
        port_status = result['scan'][ip_add_entered]['tcp'][port]['state']
        print(f"Port {port} is {port_status}")
    except:
        print(f"Cannot scan port {port}")
