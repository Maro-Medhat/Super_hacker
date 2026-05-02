#!/usr/bin/python3

import nmap

nm = nmap.PortScanner()

host = input("Enter Your Host (ex. 142.250.185.238) : ")
port = int(input("Enter Your Port (ex. 443) : "))   

result = {"tcp": False, "udp": False}

# --- TCP scan ---
nm.scan(host, str(port), arguments='-sT -Pn')
if (host in nm.all_hosts()
    and 'tcp' in nm[host]
    and port in nm[host]['tcp']      
    and nm[host]['tcp'][port]['state'] == 'open'):
    result["tcp"] = True

# --- UDP scan ---
nm.scan(host, str(port), arguments='-sU -Pn')
if (host in nm.all_hosts()
    and 'udp' in nm[host]
    and port in nm[host]['udp']      
    and nm[host]['udp'][port]['state'] in ['open', 'open|filtered']):
    result["udp"] = True

print(result)
