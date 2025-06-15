import socket

def scan_ports(ip, ports=[21, 22, 23, 80, 443, 8080]):
    print(f"\n🔍 Scanning {ip} for open ports...")
    open_ports = []
    for port in ports:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)
            result = sock.connect_ex((ip, port))
            if result == 0:
                open_ports.append(port)
            sock.close()
        except socket.error:
            pass

    if open_ports:
        print(f"✅ Open ports: {open_ports}")
    else:
        print("❌ No common open ports found.")
