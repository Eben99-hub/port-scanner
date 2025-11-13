import socket

def scan_port(ip, port):
    """Check if a port is open on a given IP"""
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        sock.connect((ip, port))
        print(f"[+] Port {port} is OPEN")
    except:
        pass
    finally:
        sock.close()

if __name__ == "__main__":
    target = input("Enter target IP address: ")
    print(f"\nScanning target: {target}\n")
    
    for port in range(1, 1025):  # scan ports 1–1024
        scan_port(target, port)
