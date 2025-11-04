Retrieve Running Configuration via SSH (Multiple Switches)
----------------------------------------------------------

This script connects to multiple Cisco switches via SSH using Paramiko,  
runs the command `show running-config`, and prints the output from each device.  
The list of device IPs is read from a local file named `switches.txt`.

Author: Islam Farraj  
Date: 2025-11-04  

Description:  
    Demonstrates how to automate the retrieval of device configurations
    from multiple Cisco switches using SSH.  
    The script loops through each switch IP, connects securely,
    runs the `show running-config` command, and prints the complete output.

Next Version:  
    The next update will enhance the script by:  
    - Saving the running configuration output into local text files  
    - Adding exception handling for unreachable or failed SSH sessions  
    - Using multithreading for faster execution across multiple devices  

---

### ✅ Python Code

```python
import paramiko
import time

# Initialize the SSH client
ssh = paramiko.SSHClient()

# Automatically accept unknown SSH host keys
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

# Read switch IPs from file
with open("switches.txt") as file:
    for line in file:
        device = line.strip()  # Clean whitespace or newline

        # Skip empty lines if any
        if not device:
            continue

        # Establish SSH connection
        ssh.connect(
            username="zz",
            password="xx",
            hostname=device,
            allow_agent=False,
            look_for_keys=False
        )

        # Start an interactive shell session
        shell = ssh.invoke_shell()
        print(f"\nConnecting to {device}...")

        # Send commands to the switch
        shell.send("terminal length 0\n")       # Prevent pagination
        time.sleep(2)
        shell.send("show running-config\n")
        time.sleep(10)                          # Wait for the switch to respond fully

        # Capture and display the output
        output = shell.recv(65535).decode()
        print(f"\n--- Output from {device} ---\n")
        print(output)

        # Close the SSH session before moving to the next switch
        ssh.close()
```
