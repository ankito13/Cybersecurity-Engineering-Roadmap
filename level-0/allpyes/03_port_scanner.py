#!/usr/bin/env python3
import socket

def scan_ports(target_ip, start_port, end_port):
    print(f"[*] Scanning {target_ip} from port {start_port} to {end_port}...")
    
    for port in range(start_port, end_port + 1):
        # Create a new socket for each port connection attempt
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(0.5) 
        
        try:
            # connect_ex returns 0 if the connection was successful
            result = s.connect_ex((target_ip, port))
            if result == 0:
                print(f"[+] Port {port} is OPEN")
        except socket.error:
            print("[!] Could not connect to server.")
            break
        finally:
            s.close()

if __name__ == "__main__":
    # Target set to localhost
    target = "8.8.8.8" 
    scan_ports(target, 20, 85)