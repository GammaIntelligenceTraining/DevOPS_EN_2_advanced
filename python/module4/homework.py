import os
import json

# ==============================================================================
# FIXTURE GENERATION (DO NOT MODIFY)
# This block automatically generates a dummy syslog file for you to parse.
# ==============================================================================
MOCK_LOG_DATA = """Oct 14 08:12:01 web01 sshd[1234]: Accepted publickey for root from 10.0.0.5
Oct 14 08:15:22 web01 sshd[1289]: Failed password for admin from 192.168.1.100
Oct 14 08:16:01 web01 systemd[1]: Started Nginx Web Server.
Oct 14 08:18:45 web01 sshd[1302]: Failed password for root from 192.168.1.100
Oct 14 08:20:10 web01 sshd[1345]: Failed password for user from 10.10.10.55
[MALFORMED_LINE_CORRUPTED_DATA]
Oct 14 08:22:33 web01 sshd[1401]: Accepted publickey for ubuntu from 10.0.0.9
Oct 14 08:25:10 web01 sshd[1450]: Failed password for admin from 192.168.1.100
"""

LOG_FILE = "syslog.txt"
OUTPUT_FILE = "audit_report.json"

if not os.path.exists(LOG_FILE):
    with open(LOG_FILE, "w") as f:
        f.write(MOCK_LOG_DATA)
    print(f"[SETUP] Created mock log file: {LOG_FILE}\n")

# ==============================================================================
# HOMEWORK: LOG AUDITOR & JSON EXPORTER
# ==============================================================================
# Scenario: You need to parse a server log, find all failed SSH login attempts,
# extract the attacker IPs, and export a JSON report.
#
# Requirements:
# 1. Use a 'try/except' block to open LOG_FILE securely. Handle FileNotFoundError.
# 2. Read the file line-by-line.
# 3. If a line contains "Failed password", extract the IP address.
#    (Hint: You can use .split() and grab the last item in the resulting list).
# 4. Wrap your extraction logic in a try/except block to catch IndexError in case
#    the log line is malformed (like our simulated corrupted line).
# 5. Keep a running tally of how many times each IP failed using a Dictionary.
# 6. Export the final Dictionary to OUTPUT_FILE as a pretty-printed JSON file.

print("Starting Audit...")
audit_results = {}

# TODO: Step 1 & 2 - Open the file defensively and iterate line-by-line

# TODO: Step 3 & 4 - Check for "Failed password", split the line safely, and extract the IP

# TODO: Step 5 - Update the audit_results dictionary tally for that IP

# TODO: Step 6 - Open OUTPUT_FILE in write mode and dump audit_results as formatted JSON

print(f"Audit Complete. Results exported to {OUTPUT_FILE}")

# ==============================================================================
# TASK 7: INTERACTIVE THREAT QUERY (while, break, continue)
# ==============================================================================
# 1. Create a `while True:` loop to keep the script running interactively.
# 2. Inside the loop, prompt the user: `ip = input("Enter IP to check (or 'q' to quit): ")`
# 3. If the user types 'q', print "Exiting query..." and use `break` to exit the loop.
# 4. If the user hits enter without typing anything (empty string ""), use `continue`
#    to immediately jump back to the prompt without crashing.
# 5. Use `.get()` to check if the entered IP exists in `audit_results`.
#    - If it does, print how many times that IP attacked.
#    - If it does not, print "IP not found in audit."

# TODO: Step 7 - Write the interactive while loop here
