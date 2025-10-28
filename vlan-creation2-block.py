"""
VLAN Configuration via SSH using Paramiko — Block Method
--------------------------------------------------------
This script connects to a Cisco switch via SSH and creates multiple
VLANs using a single block of configuration commands.

Author: Islam Farraj
Date: 2025-10-28
Description:
    - Securely connects to the device using Paramiko.
    - Sends multiple configuration commands in one block.
    - Uses a short pause after sending the full block.
    - Displays the output returned by the device.

This version is faster and cleaner than sending commands one by one.


"""

import paramiko     # Provides SSH protocol support
import getpass      # Hides password input
import time         # Adds delays to let the device process commands

# -------------------------------------------------------------
# 1. Collect login credentials securely
# -------------------------------------------------------------
host = input("Enter device IP: ")
username = input("Enter username: ")
password = getpass.getpass("Enter password: ")

# -------------------------------------------------------------
# 2. Create SSH client and connect to device
# -------------------------------------------------------------
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

ssh.connect(
    hostname=host,
    username=username,
    password=password,
    look_for_keys=False,
    allow_agent=False
)

# -------------------------------------------------------------
# 3. Open an interactive shell session
# -------------------------------------------------------------
shell = ssh.invoke_shell()

# -------------------------------------------------------------
# 4. Send all configuration commands as a single block
# -------------------------------------------------------------
commands = """
conf t
vlan 300
name test1
vlan 400
name test2
vlan 500
name test3
vlan 600
name test4
end
"""

shell.send(commands + "\n")
time.sleep(2)  # Wait for the whole block to be processed

# -------------------------------------------------------------
# 5. Capture and display device output
# -------------------------------------------------------------
print(shell.recv(5000).decode())

# -------------------------------------------------------------
# 6. Close the SSH session
# -------------------------------------------------------------
ssh.close()
