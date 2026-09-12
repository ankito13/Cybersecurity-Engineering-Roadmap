#!/usr/bin/env python3
import requests

def inspect_url(target_url):
    print(f"[*] Sending GET request to {target_url}...\n")
    
    try:
        # Adding a timeout prevents the script from hanging indefinitely 
        response = requests.get(target_url, timeout=5)
        
        print(f"[+] Status Code: {response.status_code}")
        
        print("\n[+] Server Headers:")
        # Iterating through the dictionary of HTTP headers
        for header, value in response.headers.items():
            print(f"    - {header}: {value}")
            
    except requests.exceptions.RequestException as e:
        print(f"[!] Network error occurred: {e}")

if __name__ == "__main__":
    # Using a reliable public target for testing
    target = "https://github.com"
    inspect_url(target)