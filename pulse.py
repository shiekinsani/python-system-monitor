import subprocess
from datetime import datetime

def run_cmd(command_list):
	result = subprocess.run(command_list, capture_output=True)
	return result.stdout.decode().strip()

now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

users = run_cmd(["who"])
disk = run_cmd(["df", "-h", "/"])

report = f"""
======== SERVER PULSE REPORT ============
Timestamp: {now}
-----------------------------------------
LOGGED IN USERS:
{users if users else "No other users logged in"}

DISK USAGE:
{disk}
========================================
"""

filename = f"pulse_report.txt"
with open(filename, "a") as f:
	f.write(report + "\n")

print(f"Success! Report generated in {filename}!")
