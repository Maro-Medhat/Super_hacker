#!/usr/bin/python3

import nmap

scanner = nmap.PortScanner()

ip = input("Enter Target IP : ")

scanner.scan(ip, "1-1000")

for port in scanner[ip]['tcp']:
    if scanner[ip]['tcp'][port]['state'] == 'open':
        print(f"[+] port {port}")
