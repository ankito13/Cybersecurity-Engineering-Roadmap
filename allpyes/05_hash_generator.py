#!/usr/bin/env python3
import hashlib

def generate_sha256_hash(password):
    # Encode string to bytes
    encoded_password = password.encode('utf-8')
    
    # Generate SHA-256 hash object and extract hex string
    hash_object = hashlib.sha256(encoded_password)
    return hash_object.hexdigest()

if __name__ == "__main__":
    print("[*] SHA-256 Password Hash Generator")
    user_input = input("Enter a password to hash: ")
    
    hashed_result = generate_sha256_hash(user_input)
    print(f"\n[+] Original: {user_input}")
    print(f"[+] SHA-256:  {hashed_result}")