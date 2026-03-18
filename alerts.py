import time
import os

def check_alerts(log_file="logs/alert"):
    """Continuously monitor the NIDS alert log file for new entries."""
    print(f"[*] Monitoring {log_file} for new alerts...")
    
    if not os.path.exists(log_file):
        print(f"[-] Alert log file '{log_file}' does not exist. Run setup first.")
        return

    # Basic implementation of a 'tail -f' behavior in Python
    with open(log_file, "r") as f:
        # Move the pointer to the end of the file to only catch new alerts
        f.seek(0, os.SEEK_END)
        
        try:
            while True:
                line = f.readline()
                if not line:
                    # No new data, wait briefly and check again
                    time.sleep(1)
                    continue
                
                # We found a new alert
                alert_text = line.strip()
                print(f"[ALERT DETECTED] {alert_text}")
                
                # In a more advanced system, we could parse the IP here
                # and automatically call response.block_ip(ip) -> Intrusion Prevention (IPS)
                
        except KeyboardInterrupt:
            # We catch Ctrl+C so it gracefully exits instead of throwing an error
            print("\n[*] Stopped checking alerts.")

if __name__ == "__main__":
    try:
        check_alerts()
    except KeyboardInterrupt:
        pass
