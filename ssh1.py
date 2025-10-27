"""
Simple SSH Automation Script using Paramiko
-------------------------------------------
This script connects to a Cisco network device over SSH,
executes a single command, and prints the output.

Author: Islam Farraj
Date: 2025-10-27
Description:
    Demonstrates how to establish an SSH connection,
    send a command, and read the response using Python's Paramiko library.
"""

import paramiko   # Python implementation of the SSHv2 protocol. Allows secure SSH connections.
import time       # Used to add short pauses (sleep()), giving the device time to respond.

# -------------------------------------------------------------
# 1. Create SSH client and configure connection behavior
# -------------------------------------------------------------
ssh = paramiko.SSHClient()  
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())  
# Auto-accept unknown SSH keys (avoids manual confirmation)

# -------------------------------------------------------------
# 2. Connect to the network device
# -------------------------------------------------------------
ssh.connect(
    "Replace with SW IP",
    username="your-username",
    password="your password",
    look_for_keys=False,   # Prevent Paramiko from searching for SSH private keys
    allow_agent=False      # Disable use of local SSH agents
)
# Establishes an encrypted SSH session with the target device

# -------------------------------------------------------------
# 3. Open an interactive shell and send a command
# -------------------------------------------------------------
shell = ssh.invoke_shell()  
# Opens an interactive terminal session (like PuTTY or SecureCRT)

shell.send("show ip interface brief\n")  
# Sends the command to the device (\n = press Enter)

time.sleep(2)  
# Wait for the command to finish and output to return

# -------------------------------------------------------------
# 4. Read and print the command output
# -------------------------------------------------------------
output = shell.recv(5000).decode()
# recv(5000): reads up to 5000 bytes from the device's output buffer
# decode(): converts from bytes to readable ASCII text

print(output)

# -------------------------------------------------------------
# 5. Close the SSH session
# -------------------------------------------------------------
ssh.close()

# -------------------------------------------------------------
# Next Step:
# In the next version of this script, we'll improve security
# by removing the hardcoded password and using getpass instead.
# -------------------------------------------------------------
