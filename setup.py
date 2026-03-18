import os

def setup_nids():
    """Initialize folders and configuration files for the NIDS tool (Snort/Suricata)."""
    print("[*] Setting up NIDS environment...")
    
    # Create directories for rules and logs
    os.makedirs('rules', exist_ok=True)
    os.makedirs('logs', exist_ok=True)
    
    # Create a basic snort configuration if it doesn't exist
    if not os.path.exists('snort.conf'):
        with open('snort.conf', 'w') as f:
            f.write("include $RULE_PATH/local.rules\n")
        print("[+] Created snort.conf configuration file.")
        
    # Create a blank local.rules file
    if not os.path.exists('rules/local.rules'):
        with open('rules/local.rules', 'w') as f:
            f.write("# Custom NIDS Rules\n")
        print("[+] Created rules/local.rules for custom signatures.")
        
    # Create a dummy alert file for testing if it doesn't exist
    if not os.path.exists('logs/alert'):
        with open('logs/alert', 'w') as f:
            f.write("")
            
    print("[*] Setup complete. Ready to configure rules.")

if __name__ == "__main__":
    setup_nids()
