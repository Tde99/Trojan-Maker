```
  _____ ____   ___      _   _   _   __  __    _    _  _______ ____  
 |_   _|  _ \ / _ \    | | / \ | \ | | |  \/  |  / \  | ____|  _ \ 
   | | | |_) | | | |   | |/ _ \|  \| | | |\/| | / _ \ |  _| | |_) |
   | | |  _ <| |_| | |_| / ___ \ |\  | | |  | |/ ___ \| |___|  _ < 
   |_| |_| \_\\___/ \___/_/   \_\_| \_| |_|  |_/_/   \_\_____|_| \_\
```

TROJAN-MAKER (MSFVENOM WRAPPER)
A streamlined Python automation script designed to simplify the creation of 
Metasploit payloads. This tool provides a menu-driven interface for generating 
Windows-based reverse shells, allowing security researchers to quickly prepare 
executables for authorized penetration testing scenarios.

**Features**
* **Payload Variety:** Support for common Meterpreter shells (TCP, HTTP, and HTTPS).
* **Automated Command Generation:** Eliminates the need to remember complex `msfvenom` syntax.
* **Custom Configuration:** Easily set local host (LHOST), local port (LPORT), and output filenames.
* **Visual Interface:** Uses 'figlet' to provide a clear, professional terminal environment.

**Prerequisites**
The following tools are required for the script to function correctly:
* Python 3.x
* Metasploit Framework: Specifically `msfvenom` (Must be installed).
* Figlet: (The script attempts to install this automatically via apt).

**Installation**

Clone the repository:
   * git clone https://github.com/Tde99/Trojan-Maker.git

Navigate to the directory:
   * cd Trojan-Maker

Make the script executable:
   * chmod +x trojan_maker.py

**Usage**
Generating payloads often requires system-level permissions to write files and access dependencies. Run with sudo:

sudo python3 trojan_maker.py

**How it Works:**
1. **Connection Setup:** Enter your listening IP (LHOST) and the port (LPORT) you will listen on.
2. **Payload Selection:** Choose between standard TCP connection or more stealthy HTTP/HTTPS protocols.
3. **File Generation:** The script invokes `msfvenom` to compile the payload into a Windows `.exe` format.
4. **Listener Setup:** Once the file is created, you must set up a corresponding `multi/handler` in Metasploit to receive the connection.

**Important Notes:**
* **Stealth:** Generated payloads are standard and easily detected by modern Antivirus/EDR solutions without further obfuscation.
* **Ethics & Legality:** This tool is intended strictly for authorized security auditing and educational research. Unauthorized use against systems you do not own is illegal.
* **Platform:** Designed primarily for generating Windows-target executables.
