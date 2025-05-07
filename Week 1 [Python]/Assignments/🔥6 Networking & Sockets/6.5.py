#!/usr/bin/python3

import dns.resolver

def resolve_hostname(hostname):
    try:
        # Using Google's DNS server (8.8.8.8)
        resolver = dns.resolver.Resolver()
        resolver.nameservers = ['8.8.8.8']

        # Query the DNS server to get the IP address of the hostname
        result = resolver.resolve(hostname, 'A')

        # Return the IP address (the first result)
        return result[0].to_text()

    except Exception as e:
        # Return an error if something goes wrong
        return f"Error: {str(e)}"


hostname = input("Enter a hostname : ")

ip = resolve_hostname(hostname)

print(f"IP address of {hostname} is: {ip}")


