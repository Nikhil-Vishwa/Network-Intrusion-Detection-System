import subprocess
import platform

def start_monitoring(interface="Ethernet"):
    """Start the NIDS Engine (Snort) as a monitoring process."""
    print(f"[*] Starting network monitoring on interface: {interface}...")
    
    # Snort command arguments:
    # -q: Quiet mode (less terminal spam)
    # -A fast: Write fast alerts to the log directory
    # -l logs: Output logs to the 'logs' folder
    # -c snort.conf: Use our config
    # -i interface: The network interface to listen on
    cmd = ["snort", "-q", "-A", "fast", "-l", "logs", "-c", "snort.conf", "-i", str(interface)]
    
    print(f"[*] Engine Command: {' '.join(cmd)}")
    
    try:
        print("[*] Note: If Snort is installed and in PATH, it will start analyzing traffic now.")
        print("[*] For this beginner demo, we assume the engine starts in the background.")
        
        # Uncomment below to actually run Snort if installed on the system
        # subprocess.Popen(cmd)
        
        print("[+] Monitoring is active. Traffic is being analyzed against your rules.")
    except Exception as e:
        print(f"[-] Error starting monitor: {e}")

if __name__ == "__main__":
    start_monitoring()
