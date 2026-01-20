# Python System Pulse Monitor

A lightweight system monitoring automation tool built with Python and Linux (WSL). This project demonstrates the ability to interact with the Linux Operating System, handle data processing, and schedule automated tasks.

## 🚀 Features
- **Automated Logging:** Captures system snapshots (timestamp, logged-in users, and disk usage).
- **Subprocess Integration:** Uses Python's `subprocess` module to execute and capture native Linux commands.
- **Data Decoding:** Handles Byte-to-String conversion for standard output (stdout).
- **Scheduled Monitoring:** Fully automated via **Cron Jobs** to run without human intervention.

## 🛠️ Technical Skills Demonstrated
- **Language:** Python 3
- **Environment:** Linux (Ubuntu/WSL)
- **Linux Administration:** Crontab scheduling, Absolute paths, and Shell commands (`who`, `df`).
- **DevOps Concept:** Automation of routine health checks.

## 📁 How It Works
The script `pulse.py` executes system commands and parses the output. The results are appended to a `pulse_report.txt` file, creating a historical log of the server's health status.

### Example Output:
```text
======= SERVER HEALTH REPORT =======
Timestamp: 2026-01-20 12:00:01
------------------------------------
LOGGED IN USERS:
No users logged in

DISK DETAILS:
Filesystem      Size  Used Avail Use% Mounted on
rootfs          223G   76G  148G  34% /
====================================
