import os

def add_rule(rule):
    """Append a new detection rule to the local.rules file."""
    rule_file = 'rules/local.rules'
    
    # Ensure the directory exists
    if not os.path.exists('rules'):
        os.makedirs('rules')
        
    with open(rule_file, 'a') as f:
        f.write(f"{rule}\n")
    print(f"[+] Rule added: {rule}")

def configure_basic_rules():
    """Configure some default basic detection rules."""
    print("[*] Configuring basic Snort detection rules...")
    
    # Example 1: Detect ICMP (Ping) Sweeps
    add_rule('alert icmp any any -> any any (msg:"ICMP Ping Detected"; sid:1000001; rev:1;)')
    
    # Example 2: Detect SSH connection attempts (port 22)
    add_rule('alert tcp any any -> any 22 (msg:"SSH Connection Attempt"; flags:S; sid:1000002; rev:1;)')
    
    # Example 3: Detect HTTP GET requests
    add_rule('alert tcp any any -> any 80 (msg:"HTTP GET Request"; flow:to_server; content:"GET"; sid:1000003; rev:1;)')
    
    print("[*] Base rules configured successfully.")

if __name__ == "__main__":
    configure_basic_rules()
