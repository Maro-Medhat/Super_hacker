#!/usr/bin/python3

import nmap

nm = nmap.PortScanner()

target = "127.0.0.1"

print(f"[+] Scanning {target} for listening ports...\n")

# Scan TCP + UDP, reserved + high ports
nm.scan(target, arguments='-sT -sU -Pn')

# ---- TCP Results ----
if 'tcp' in nm[target]:
    print("[TCP]")
    for port, info in nm[target]['tcp'].items():
        if info['state'] == 'open':
            print(f"  {port}/tcp  OPEN")

# ---- UDP Results ----
if 'udp' in nm[target]:
    print("\n[UDP]")
    for port, info in nm[target]['udp'].items():
        if info['state'] in ('open', 'open|filtered'):
            print(f"  {port}/udp  {info['state'].upper()}")
