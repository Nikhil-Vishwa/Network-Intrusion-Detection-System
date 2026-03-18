import sys
import setup
import rules
import monitor
import alerts
import response

def print_menu():
    print("\n" + "="*50)
    print("   🛡️ Basic Network Intrusion Detection System 🛡️")
    print("="*50)
    print("1. Setup NIDS Environment")
    print("2. Configure Default Detection Rules")
    print("3. Start Traffic Monitor Engine")
    print("4. Watch Alerts (Real-Time)")
    print("5. Test Incident Response (Block IP)")
    print("6. Exit Control Panel")
    print("="*50)

def main():
    while True:
        print_menu()
        choice = input("Select a module to execute [1-6]: ")
        
        if choice == '1':
            setup.setup_nids()
            
        elif choice == '2':
            rules.configure_basic_rules()
            
        elif choice == '3':
            interface = input("Enter network interface (e.g., 'Ethernet' or '1'): ")
            if not interface:
                interface = "Ethernet"
            monitor.start_monitoring(interface)
            
        elif choice == '4':
            print("\n[*] Changing to Alert Watcher Mode. (Press Ctrl+C to return to menu)")
            try:
                alerts.check_alerts()
            except KeyboardInterrupt:
                print("\n[*] Returned to main menu.")
                
        elif choice == '5':
            ip_to_block = input("Enter simulated attacker IP to block: ")
            if ip_to_block:
                response.block_ip(ip_to_block)
                response.log_incident(ip_to_block, "Manual Response Intervention")
                
        elif choice == '6':
            print("[*] Shutting down NIDS Control Panel. Stay secure!")
            sys.exit(0)
            
        else:
            print("[-] Invalid selection. Please enter a number from 1 to 6.")

if __name__ == "__main__":
    print("[*] Booting up NIDS...")
    main()
