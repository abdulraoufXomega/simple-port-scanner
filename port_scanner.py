import socket
import time

# Define the target and port range
target = input("Enter the target IP address: ")
port_range = input("Enter the port range (e.g., 1-100): ")
start_port, end_port = map(int, port_range.split('-'))

# Function to scan a single port
def scan_port(port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.5)
        result = sock.connect_ex((target, port))
        if result == 0:
            print(f"Port {port}: Open")
        else:
            print(f"Port {port}: Closed")
        sock.close()
    except Exception as e:
        print(f"Error scanning port {port}: {e}")

# Start scanning
print(f"Scanning target {target}...")
start_time = time.time()

for port in range(start_port, end_port + 1):
    scan_port(port)

end_time = time.time()
print(f"Scan completed in {end_time - start_time:.2f} seconds")