Retrieve and Save Running Configurations (Single Output File)
-------------------------------------------------------------

This script connects to multiple Cisco switches via SSH using the Paramiko library.  
It runs the `show running-config` command on each switch and saves **all outputs**  
together into a single local text file named **`output.txt`**.

Author: Islam Farraj  
Date: 2025-11-04  

Description:  
    This script demonstrates reading multiple device IPs from a file (`switches.txt`),
    connecting to each device via SSH, executing a command, and writing the results
    from all devices into one consolidated output file.
    
    Each switch output is separated by clear section headers for readability.

Next Version:  
    The next update will:
    - Add a timestamp to the output file name (e.g., `output_20251104.txt`)
    - Later, save each switch’s output in its own separate file with timestamps
    - Include error handling for offline or unreachable devices

---

### ✅ Python Code

```python
import paramiko
import time

# Initialize SSH client
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

# Open (or create) a single file to store outputs from all switches
with open("output.txt", "w") as save_file:
    # Read device IPs from file
    with open("switches.txt") as file:
        for line in file:
            device = line.strip()

            # Skip empty lines if any
            if not device:
                continue

            print(f"\nConnecting to {device}...")

            # Establish SSH connection
            ssh.connect(
                username="xx",
                password="yy",
                hostname=device,
                allow_agent=False,
                look_for_keys=False
            )

            # Open an interactive shell session
            shell = ssh.invoke_shell()
            shell.send("terminal length 0\n")
            time.sleep(2)
            shell.send("show running-config\n")
            time.sleep(10)

            # Read output from the switch
            output = shell.recv(65535).decode()

            # Write switch output to the same file
            save_file.write(f"\n\n=== Output from {device} ===\n")
            save_file.write(output)
            save_file.write("\n" + "=" * 50 + "\n")

            print(f"✅ Saved output for {device} to output.txt")

            ssh.close()

print("\n✅ All switch outputs have been saved to output.txt")
```

---

### 🗂️ Example Files

**`switches.txt`**
```
10.8.94.3
10.8.94.4
10.8.94.5
```

**`output.txt`**
```
=== Output from 10.8.94.3 ===
<switch config here>
==================================================
=== Output from 10.8.94.4 ===
<switch config here>
==================================================
```

---
