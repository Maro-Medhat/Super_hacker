#!/usr/bin/python3

import ipaddress

def isIPv6(ip):
  try:
    ip_obj = ipaddress.ip_address(ip)
    if ip_obj.version == 6:
      return True
  except ValueError:
    return False

def ipv6_forms(ip):
  ip_obj = ipaddress.ip_address(ip)
  print(f"[+] {ip} -> Compressed: {ip_obj.compressed}")
  print(f"[+] {user_ip} -> Expanded: {ip_obj.exploded}")

user_ip = input("Enter an IPv6 : ").strip();

if isIPv6(user_ip):
  ipv6_forms(user_ip)
else:
  print(f"[!] {user_ip} -> Invalid!!")