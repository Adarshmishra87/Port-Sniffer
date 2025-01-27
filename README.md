Port Scanner
This is a simple Python script that scans a range of ports on a given target IP address to check whether they are open or closed.

Features
Scans ports from 20 to 1024.
Uses Python's socket library to attempt to connect to each port.
Provides the status of each port (open or closed).
Timeout of 1 second for connection attempts to avoid long delays.
Installation
To use this script, you need to have Python 3.x installed on your machine. No external libraries are required as it uses Python's built-in libraries.

Clone the repository:

bash
Copy
git clone https://github.com/yourusername/port-scanner.git
Navigate into the project directory:

bash
Copy
cd port-scanner
Usage
To use the port scanner, you need to modify the target_ip variable with the IP address you want to scan. The script will then check the range of ports from 20 to 1024 on that target.

Open the port_scanner.py file and modify the target_ip to your desired target.

Run the script:

bash
Copy
python port_scanner.py
The script will output whether each port in the range is open or closed.

Example
If you're scanning the IP 192.168.1.1, the output will look like this:

bash
Copy
Scanning ports on 192.168.1.1...
Port 20 is closed.
Port 21 is open.
Port 22 is open.
Port 23 is closed.
...
Customization
Timeout: The timeout for each connection attempt is set to 1 second by default. You can change this by modifying the sock.settimeout(1) line in the code.

Port Range: The script scans ports from 20 to 1024. You can change the range by modifying the for port in range(20, 1025) line.
