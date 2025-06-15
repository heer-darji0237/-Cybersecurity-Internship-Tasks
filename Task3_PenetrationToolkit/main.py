from port_scanner import scan_ports
from brute_forcer import brute_force_login

def main():
    print("\n🔧 Penetration Testing Toolkit")
    print("1. Port Scanner")
    print("2. Brute-Force Login")
    print("3. Exit")

    choice = input("Choose a tool (1/2/3): ")

    if choice == "1":
        ip = input("Enter target IP address: ")
        scan_ports(ip)
    elif choice == "2":
        url = input("Enter login form URL: ")
        username = input("Enter username to brute force: ")
        wordlist = input("Enter path to wordlist (e.g., wordlist.txt): ")
        brute_force_login(url, username, wordlist)
    elif choice == "3":
        print("👋 Exiting...")
    else:
        print("❌ Invalid choice!")

if __name__ == "__main__":
    main()
