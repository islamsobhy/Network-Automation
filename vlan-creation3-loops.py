"""
Network Automation with Paramiko
--------------------------------
This script connects to a network switch using SSH and creates
10 VLANs dynamically using a Python for-loop.

Author: Islam Farraj
"""

import paramiko       # Secure SSH communication
import getpass        # Hides password input
import time           # Used for small delays between commands

# --- Get user input ---
host = input("Enter device IP: ")
username = input("Enter SSH username: ")
password = getpass.getpass("Enter SSH password: ")

# --- Create SSH connection ---
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())  # Auto-accept unknown host keys

ssh.connect(
    hostname=host,
    username=username,
    password=password,
    look_for_keys=False,
    allow_agent=False
)

# --- Start interactive shell session ---
shell = ssh.invoke_shell()

# Enter configuration mode
shell.send("conf t\n")
time.sleep(1)

# --- Create VLANs using a loop ---
for vlan_id in range(300, 310):  # VLANs 300 to 309
    shell.send(f"vlan {vlan_id}\n")
    time.sleep(0.3)
    shell.send(f"name VLAN_{vlan_id}\n")
    time.sleep(0.3)

# Exit configuration mode
shell.send("end\n")
time.sleep(1)

# --- Read and display output from the switch ---
if shell.recv_ready():
    output = shell.recv(5000).decode()
    print(output)

# --- Close SSH session ---
ssh.close()
