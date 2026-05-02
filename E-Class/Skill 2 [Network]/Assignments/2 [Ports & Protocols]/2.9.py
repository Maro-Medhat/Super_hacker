#!/usr/bin/python3

import nmap

host = input("Enter host (ex. 127.0.0.1): ").strip()

nm = nmap.PortScanner()

# Scan UDP ports 1–1024
nm.scan(host, arguments='-sU -Pn')

if 'udp' in nm[host]:
    for port, info in nm[host]['udp'].items():
        state = info['state']
        if state in ('open', 'open|filtered'):
            print(f"[+] {port}/udp  {state.upper()}")