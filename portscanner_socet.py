#!/usr/bin/env python3

import socket
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

open_ports = []

while True:
    ip_add_entered = input("\nEnter target IP address: ")
    if ip_add_pattern.search(ip_add_entered):
        break
    else:
        print("Invalid IP address format.")

while True:
    port_range = input("Enter port range (e.g. 20-100): ")
    match = port_range_pattern.search(port_range.replace(" ", ""))
    if match:
        port_min = int(match.group(1))
        port_max = int(match.group(2))
        break
    else:
        print("Invalid port range format.")

for port in range(port_min, port_max + 1):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(0.5)
            s.connect((ip_add_entered, port))
            open_ports.append(port)
    except:
        pass

if open_ports:
    for port in open_ports:
        print(f"Port {port} is OPEN on {ip_add_entered}")
else:
    print("No open ports found.")
