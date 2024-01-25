# This Code Made by D3F417
# Github : https://github.com/mss-d3f417
# Don't Copy Script KIDI 

import bluetooth

def scan_bluetooth_devices():
    try:
        
        discovered_devices = bluetooth.discover_devices(lookup_names=True, lookup_class=True)
        
        
        print('[!] Scanning for active devices...')
        print(f"[!] Found {len(discovered_devices)} Devices\n")

        
        for addr, name, device_class in discovered_devices:
            print(f'[+] Name: {name}')
            print(f'[+] Address: {addr}')
            print(f'[+] Device Class: {device_class}\n')
    
    except Exception as e:
        
        print(f"[ERROR] An error occurred: {e}")



scan_bluetooth_devices()