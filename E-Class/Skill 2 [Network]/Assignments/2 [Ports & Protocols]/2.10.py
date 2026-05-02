#!/usr/bin/python3

common_ports = {
    20:  "FTP-Data",
    21:  "FTP",
    22:  "SSH",
    23:  "Telnet",
    25:  "SMTP",
    53:  "DNS",
    67:  "DHCP-Server",
    68:  "DHCP-Client",
    69:  "TFTP",
    80:  "HTTP",
    110: "POP3",
    111: "RPCbind",
    135: "Microsoft RPC",
    137: "NetBIOS Name Service",
    138: "NetBIOS Datagram Service",
    139: "NetBIOS Session Service",
    143: "IMAP",
    161: "SNMP",
    389: "LDAP",
    443: "HTTPS",
    445: "SMB",
    514: "Syslog",
    873: "rsync",
    993: "IMAPS",
    995: "POP3S"
}

for key, value in common_ports.items():
    print(f"{key} => {value}")
