Multi-Device VLAN Configuration via SSH using Paramiko
------------------------------------------------------

This script connects to multiple Cisco switches over SSH using Paramiko.  
It reads switch IPs from a text file (`switches.txt`), enters configuration mode,  
and creates multiple VLANs (with names) on each switch.

Author: Islam Farraj  
Date: 2025-11-04  

Description:  
    This script demonstrates how to use nested loops in Python to automate
    VLAN creation across multiple devices.  
    - The outer loop iterates through each switch IP from a text file.  
    - The inner loop creates and names VLANs sequentially (e.g., VLAN 600–609).  
    The script opens an SSH session, sends configuration commands, and
    prints confirmation output from each device.

Next Version:  
    The next update will group all VLAN commands into one configuration block
    and send them at once (instead of one-by-one).  
    This improves performance and minimizes SSH round trips per device.

---

### ✅ Python Code

```python
import paramiko
import getpass
import time

# Create SSH client object
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

# Secure password entry
password = getpass.getpass("Enter your SSH password: ")

# Read switch IPs from file and loop through each device
with open("switches.txt") as file:
    for line in file:
        device = line.strip()  # Remove spaces/newlines

        # Skip empty lines if any
        if not device:
            continue

        # Connect to each switch using SSH
        ssh.connect(
            hostname=device,
            username="x",       # Replace with your username
            password=password,
            look_for_keys=False,
            allow_agent=False
        )

        # Start interactive shell session
        shell = ssh.invoke_shell()
        shell.send("conf t\n")
        time.sleep(1)

        # Inner loop: Create VLANs 600–609 with names
        for vlan in range(600, 610):
            shell.send(f"vlan {vlan}\n")
            time.sleep(0.5)
            shell.send(f"name vlan_{vlan}\n")
            time.sleep(0.5)

        # Exit configuration mode
        shell.send("end\n")
        time.sleep(1)

        # Receive and display device output
        output = shell.recv(5000).decode()
        print(f"\n--- VLANs created on {device} ---")
        print(output)

        # Close SSH connection before next switch
        ssh.close()
```
