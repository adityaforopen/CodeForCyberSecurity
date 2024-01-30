# port_scanner.py

import socket

def scan_ports(target, start_port, end_port):
    print(f"Scanning ports on {target}...")
    for port in range(start_port, end_port + 1):
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)
            result = sock.connect_ex((target, port))
            if result == 0:
                print(f"Port {port} is open")
            sock.close()
        except KeyboardInterrupt:
            print("\nScan interrupted by user")
            return
        except socket.gaierror:
            print("Hostname could not be resolved")
            return
        except socket.error:
            print("Couldn't connect to server")
            return
    print("Port scanning complete")

if __name__ == "__main__":
    target_host = input("Enter target host: ")
    start_port = int(input("Enter start port: "))
    end_port = int(input("Enter end port: "))
    scan_ports(target_host, start_port, end_port)
