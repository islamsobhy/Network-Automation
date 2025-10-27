"""
Secure SSH Automation Script using Paramiko
-------------------------------------------
This script connects to a Cisco network device over SSH,
executes a command, and prints the output.
Unlike the previous version, this script does not store
the password directly in the code — it prompts the user
for credentials securely at runtime.

Author: Your Name
Date: YYYY-MM-DD
Description:
    Demonstrates a simple, secure SSH connection to a network
    device using Python's Paramiko library and the getpass module.
"""

import paramiko    # Python implementation of the SSHv2 protocol (for SSH connections)
import time        # Used for short pauses (sleep) to allow command execution
import getpass     # Provides secure password input (not visible while typing)

# -------------------------------------------------------------
# 1. Collect connection details securely
# -------------------------------------------------------------
host = input("Enter device IP address: ")
username = input("Enter your username: ")
password = getpass.getpass("Enter your password: ")
# getpass hides the password as you type for better security

# -------------------------------------------------------------
# 2. Create SSH client and configure behavior
# -------------------------------------------------------------
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# Automatically accept the device’s SSH key (avoids manual confirmation)

# -------------------------------------------------------------
# 3. Establish SSH connection to the device
# -------------------------------------------------------------
ssh.connect(
    hostname=host,
    username=username,
    password=password,
    look_for_keys=False,   # Prevent searching for local SSH keys
    allow_agent=False      # Disable use of local SSH agents
)
# At this point, the script has successfully authenticated to the device

# -------------------------------------------------------------
# 4. Open interactive shell and send command
# -------------------------------------------------------------
shell = ssh.invoke_shell()  
# Opens an interactive session (like typing commands manually)

shell.send("show ip interface brief\n")  
# Sends a command to the device

time.sleep(2)  
# Waits for the device to process and respond

# -------------------------------------------------------------
# 5. Capture and display output
# -------------------------------------------------------------
output = shell.recv(5000).decode()
print(output)

# -------------------------------------------------------------
# 6. Close the SSH session
# -------------------------------------------------------------
ssh.close()

# -------------------------------------------------------------
# Next Step:
# In the following version, we’ll expand this script to send
# multiple commands and save their output to a text file.
# -------------------------------------------------------------
