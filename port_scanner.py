import _socket
import time


# Function to get the protocol name
def get_protocol_name(port):
    try:
        return _socket.getservbyport(port)
    except:
        return "Unknown"

# Define the target and port range
try:
    target = input("Enter the target IP address: ")
    port_range = input("Enter the port range (e.g., 1-100): ")
    start_port, end_port = map(int, port_range.split('-'))
except ValueError:
    print("INVALID INPUT!!. Please enter a valid IP address and port range.")
    exit(1)

# Function to scan a single port
def scan_port(port):
    try:
        sock = _socket.socket(_socket.AF_INET, _socket.SOCK_STREAM)
        sock.settimeout(0.1)
        result = sock.connect_ex((target, port))
        if result == 0:
            protocol = get_protocol_name(port)
            print(f"Port {port} ({protocol}): Open")
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