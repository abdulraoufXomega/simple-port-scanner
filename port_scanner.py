# Port Scanner.
# Author: Abdulraouf_Almaaloul.
# Description: A simple TCP port scanner that checks for open ports on a target IP address.
import _socket
import time


# Function to get the protocol name.
def get_protocol_name(port):
    try:
        # Returns a pointer to the structure.
        return _socket.getservbyport(port)
    except:
        # Otherwise it's going to return "Unknown".
        return "Unknown"

# Define the target and port range.
try:
    # Gets the IP address as input from the user.
    target = input("Enter the target IP address: ")
    # Gets the IP address as input from the user.
    port_range = input("Enter the port range (e.g., 1-100): ")
    # Splitting the port range with hyphen for each one of it.
    start_port, end_port = map(int, port_range.split('-'))
except ValueError:
    print("INVALID INPUT!!. Please enter a valid IP address and port range.")
    exit(1)

# Function to scan a single port.
def scan_port(port):
    try:
        # Create a socket object.
        sock = _socket.socket(_socket.AF_INET, _socket.SOCK_STREAM)
        # Set a timeout to avoid annoying hanging.
        sock.settimeout(0.1)
        # Connect to the target port.
        result = sock.connect_ex((target, port))
        if result == 0:
            # Retrieving protocol name for each scan.
            protocol = get_protocol_name(port)
            # Print out every port along with the associated protocol.
            print(f"Port {port} ({protocol}): Open")
        sock.close()
    except Exception as e:
        print(f"Error scanning port {port}: {e}")

# Start scanning
print(f"Scanning target {target}...")
start_time = time.time()

# Looping through the specified port range
for port in range(start_port, end_port + 1):
    scan_port(port)

# Calculate and display the total scan time.
end_time = time.time()
print(f"Scan completed in {end_time - start_time:.2f} seconds")
