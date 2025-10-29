# ------------------------------------------------------------
# Multi-Device SSH Automation using Paramiko
# ------------------------------------------------------------
# This script connects to a list of switches and runs commands.
# It reads the IPs from a text file (switches.txt) — one IP per line.
# ------------------------------------------------------------

import paramiko          # Library that lets Python use SSH to connect securely to network devices
import getpass           # Used for hiding the password when typing
import time              # Used for short pauses to let devices respond

# --- Step 1: Get user credentials ---
username = input("Enter your SSH username: ")
password = getpass.getpass("Enter your SSH password: ")

# --- Step 2: Open and read the device list ---
# The file 'switches.txt' should have one IP address per line, like:
# 10.32.94.4
# 10.32.94.5
# 10.32.94.6
with open("switches.txt") as file:
    for line in file:
        host = line.strip()  # Removes spaces and newline characters
        print(f"\n🔗 Connecting to {host}...")

        # --- Step 3: Create and configure the SSH client ---
        ssh = paramiko.SSHClient()                          # Create a new SSH client object
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())  # Automatically add unknown host keys

        # --- Step 4: Connect to the device ---
        ssh.connect(
            hostname=host,
            username=username,
            password=password,
            look_for_keys=False,
            allow_agent=False
        )

        # --- Step 5: Open a shell session and send commands ---
        shell = ssh.invoke_shell()
        shell.send("show ip interface brief\n")
        time.sleep(1)  # Give the switch a second to respond

        # --- Step 6: Receive and print the command output ---
        output = shell.recv(5000).decode()  # Read up to 5000 bytes of output and convert to text
        print(f"🖥️ Output from {host}:\n{output}")

        # --- Step 7: Close the SSH session ---
        ssh.close()
        print(f"✅ Connection to {host} closed.\n")

# ------------------------------------------------------------
# End of Script
# ------------------------------------------------------------
# Next step idea:
# You can replace the command block with a configuration section
# (e.g., creating VLANs or updating interface descriptions)
# ------------------------------------------------------------
