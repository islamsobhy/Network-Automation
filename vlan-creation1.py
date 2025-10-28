"""
VLAN Configuration via SSH using Paramiko
-----------------------------------------
This script connects to a Cisco network device over SSH and
creates multiple VLANs one by one.

Author: Your Name
Date: YYYY-MM-DD
Description:
    Demonstrates how to log in to a network device using Paramiko,
    enter configuration mode, and send multiple configuration
    commands sequentially with timed delays.

Next Version:
    The next script will improve efficiency by grouping all
    configuration commands into a single block and sending them
    together instead of one by one.
"""

import paramiko     # Provides SSH protocol support
import getpass      # Hides password input
import time         # Adds short pauses to let the device process commands

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
# 4. Send configuration commands (with short pauses)
# -------------------------------------------------------------
shell.send("conf t\n")
time.sleep(1)

shell.send("vlan 300\n")
time.sleep(0.5)
shell.send("name test1\n")
time.sleep(0.5)

shell.send("vlan 400\n")
time.sleep(0.5)
shell.send("name test2\n")
time.sleep(0.5)

shell.send("vlan 500\n")
time.sleep(0.5)
shell.send("name test3\n")
time.sleep(0.5)

shell.send("vlan 600\n")
time.sleep(0.5)
shell.send("name test4\n")
time.sleep(0.5)

shell.send("end\n")
time.sleep(1)

# -------------------------------------------------------------
# 5. Capture and display device output
# -------------------------------------------------------------
print(shell.recv(5000).decode())

# -------------------------------------------------------------
# 6. Close the SSH session
# -------------------------------------------------------------
ssh.close()
