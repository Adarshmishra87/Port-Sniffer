# Port Scanner

A simple Python script for scanning ports on a given IP address to check whether they are open or closed. This tool helps in network diagnostics and security assessments.

---

## 🚀 Features

- Scans ports in the range from **20** to **1024**.
- Checks if a port is **open** or **closed**.
- Uses Python's built-in **socket** library for efficient network communication.
- Configurable **timeout** of 1 second to prevent long delays during port checks.
- Easy to modify for custom port ranges and timeouts.

---

## 📦 Installation

This script is written in Python 3.x and doesn't require any additional dependencies. Just ensure you have Python 3 installed.

1. **Clone the repository**:
   ```bash
   git clone https://github.com/Adarshmishra87/port-scanner.git
   ```

2. **Navigate into the project directory**:
   ```bash
   cd port-scanner
   ```

---

## 🧑‍💻 Usage

To use the port scanner, you need to specify the target IP address you want to scan. The script will check ports from 20 to 1024 on that IP.

1. **Edit the `target_ip`** in the script to the desired IP address.
   ```python
   target_ip = "192.168.1.1"
   ```

2. **Run the script**:
   ```bash
   python port_scanner.py
   ```

The script will output a list of ports and their status (open or closed).

---

## 📊 Output

```bash
Scanning ports on 192.168.1.1...
Port 20 is closed.
Port 21 is open.
Port 22 is open.
Port 23 is closed.
Port 24 is closed.
...
```

---

## 🔧 Customization

- **Port Range**: By default, the script scans ports from **20** to **1024**. You can adjust this range by modifying the `for port in range(20, 1025)` line.
- **Timeout**: The connection timeout is set to **1 second** by default. You can adjust this in the line `sock.settimeout(1)` if needed.
  
---
