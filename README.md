# Port Scanner

A simple utility act as a port scanner built using Python. This tool scans a target IP address for open, closed, or filtered ports within a specified range.

---

## Features
- Scans a range of ports on a target IP address.
- Supports TCP port scanning.
- Displays open ports only.
- Measures the time taken for the scan.

---

## How It Works
The port scanner uses Python's `socket` library to establish TCP connections with the target ports. It attempts to connect to each port in the specified range and determines whether the port is open or closed based on the connection result.

---

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/port-scanner.git
   ```

## Navigation
2. Navigate to the project directory:
   ```bash
   cd port-scanner
   ```

## Execution
3. Run the port scanner:
   ```bash
   python port_scanner.py
   ```
---

## Key Components
1. ### Socket Library: Used to establish TCP connections.
2. ### Port Range: The user specifies the range of ports to scan.
3. ### Timeout: A timeout of 0.1 seconds is set to avoid hanging on un responsive ports.
4. ### Result Analysis: The "connect_ex" method returns '0' if the port is open.

---

## Future Enhancements
- Add support for UDP scanning.
- Implement multithreading for faster scans.
- Add banner grabbing to identify services running on open ports.
- Save scan results.

---
