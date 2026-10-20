"""
Module 6 Homework: Microservice Uptime Monitor

Scenario:
You are tasked with writing a monitoring script that audits a list of internal microservice URLs. 
Your script must loop through the endpoints, attempt to connect, and log whether the service 
is UP (200 OK), DOWN (other status codes), or UNREACHABLE (Timeout / DNS failures).

Requirements:
1. Iterate over the `SERVICES` list.
2. Perform a `requests.get()` on each URL.
3. Enforce a strict `timeout` of 3 seconds to prevent the script from hanging.
4. If the request is successful (Status 200), print "[OK] [URL] is UP".
5. If the request returns a bad status code (e.g., 404, 500), print "[WARN] [URL] is DOWN (Status: X)".
6. If the request throws a network exception (Timeout or Connection Error), catch it using 
   `requests.exceptions.RequestException` and print "[ERROR] [URL] is UNREACHABLE".
7. Keep a count of how many services are UP and print a final summary report.
"""

import requests

# Starter Variables (Fixtures)
SERVICES = [
    "https://api.github.com",                                # Should be UP
    "https://httpstat.us/404",                               # Will return a 404 Not Found
    "https://httpstat.us/500",                               # Will return a 500 Server Error
    "https://httpstat.us/200?sleep=5000",                    # Will trigger a Timeout (sleeps for 5s)
    "https://this-domain-definitely-does-not-exist.com"      # Will trigger a DNS/Connection exception
]

print("Starting Microservice Uptime Audit...\n")
print("-" * 40)

up_count = 0

# TODO: Create a for loop to iterate over SERVICES
# TODO: Inside the loop, use a try/except block.
# TODO: Perform a GET request with a 3-second timeout.
# TODO: Check the status code and print the appropriate message.
# TODO: Catch requests.exceptions.RequestException and print the Unreachable message.

print("-" * 40)
# TODO: Print the final summary (e.g., "Audit Complete. 1/5 services are UP.")
