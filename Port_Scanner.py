import socket
from datetime import datetime

def scan_port(host, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)  # Timeout for connection attempts
    result = sock.connect_ex((host, port))
    if result == 0:
        print(f"Port {port} is open.")
    else:
        print(f"Port {port} is closed.")
    sock.close()
def scan_ports(target):
    print(f"Scanning ports on {target}...")
    for port in range(20, 1025):
        scan_port(target, port)

if __name__ == "__main__":
    target_ip = "192.168.1.1"
    scan_ports(target_ip)
