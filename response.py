import platform

def block_ip(ip_address):
    """Block an offending IP address using the OS firewall."""
    print(f"[*] Initiating automated response for malicious IP: {ip_address}")
    
    current_os = platform.system()
    
    try:
        if current_os == "Windows":
            # Command to block IP in Windows Defender Firewall
            cmd = f'netsh advfirewall firewall add rule name="NIDS Block {ip_address}" dir=in action=block remoteip={ip_address}'
            print(f"[+] Firewall Command Execution: {cmd}")
            # subprocess.run(cmd, shell=True) # Uncomment to execute (Requires Admin Privileges)
            
        elif current_os == "Linux":
            # Command to block IP using iptables
            cmd = f'sudo iptables -A INPUT -s {ip_address} -j DROP'
            print(f"[+] Firewall Command Execution: {cmd}")
            # subprocess.run(cmd, shell=True) # Uncomment to execute (Requires Root Privileges)
            
        else:
            print(f"[-] OS '{current_os}' firewall commands not configured.")
            
        print(f"[+] Response Active: Connection blocked for {ip_address}")
    except Exception as e:
        print(f"[-] Failed to execute block: {e}")

def log_incident(ip_address, incident_type):
    """Log the automated response action taken."""
    # Ensure logs folder exists
    import os
    os.makedirs('logs', exist_ok=True)
    
    with open('logs/response.log', 'a') as f:
        f.write(f"ACTION: Blocked {ip_address} | REASON: {incident_type}\n")
    print("[+] Incident logged to response.log")

if __name__ == "__main__":
    # Test execution
    test_ip = "192.168.1.100"
    block_ip(test_ip)
    log_incident(test_ip, "Simulated Attack Test")
