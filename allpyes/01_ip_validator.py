#!/usr/bin/env python3
import ipaddress
target = input("Enter an IP address to validate: ")

try:
    ip = ipaddress.ip_address(target)
    print(f"[SUCCESS] {ip} is a valid IPv4/IPv6 address.")
except ValueError:
    print(f"[ERROR] {target} is NOT a valid IP address.")
