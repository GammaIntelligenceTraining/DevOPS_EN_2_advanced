import sys
import re

print("=" * 70)
print("MODULE 5: Regular Expressions, System Basics & Functional Tools")
print("=" * 70)

print("\nSECTION 1: Advanced String Parsing with Regex (re)")
print("-" * 70)
# Regular expressions allow us to search for PATTERNS in text, not just exact words.
# We always use 'r' (raw string) before the quote (e.g., r"pattern") so Python reads it literally.

sample_log = "2023-10-25 14:32:01 - ERROR - User admin logged in from 192.168.1.105 with status 403."

# 1.1 re.search() - Finding the FIRST match
print("--- 1.1 re.search() ---")
# Pattern: \d{3} means "exactly 3 digits"
match = re.search(r"\d{3}", sample_log)
if match:
    # .group() returns the actual string that matched the pattern
    print(f"Found a 3-digit number: {match.group()}") 
else:
    print("No 3-digit number found.")

# 1.2 re.findall() - Extracting ALL matches into a List
print("\n--- 1.2 re.findall() ---")
# Pattern: \d+ means "one or more digits"
all_numbers = re.findall(r"\d+", sample_log)
print(f"All numbers found in the log: {all_numbers}")

# Pattern for a basic IP address: 
# \d{1,3} = 1 to 3 digits
# \. = a literal dot (escaped, because a normal dot means 'any character')
ip_pattern = r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}"
all_ips = re.findall(ip_pattern, sample_log)
print(f"Extracted IPs: {all_ips}")

# 1.3 re.sub() - Replacing / Masking patterns
print("\n--- 1.3 re.sub() ---")
# We want to redact the IP address from the log for security
redacted_log = re.sub(ip_pattern, "[REDACTED_IP]", sample_log)
print(f"Original: {sample_log}")
print(f"Redacted: {redacted_log}")
# 1.4 Pattern Matching: Boundaries, Sets, Escapes, and Complex Regex
print("\n--- 1.4 Advanced Patterns ---")
log_line = "ERROR: Failed to connect to db at 10.0.0.1! catalog connection lost."

# Exact text match & Anchors
print(f"Literal text 'connect' found: {bool(re.search(r'connect', log_line))}")
print(f"Starts with ERROR: {bool(re.search(r'^ERROR', log_line))}")

# Word Boundaries: \b ensures we only match whole words
print(f"Standalone 'cat' found (bypassing 'catalog'): {bool(re.search(r'\bcat\b', log_line))}")

# Character Sets: [] and ranges
alphanumeric_str = "user123_ADMIN!?"
print(f"Lowercase [a-z]: {re.findall(r'[a-z]+', alphanumeric_str)}")
print(f"Uppercase [A-Z]: {re.findall(r'[A-Z]+', alphanumeric_str)}")
print(f"Digits [0-9]: {re.findall(r'[0-9]+', alphanumeric_str)}")
print(f"Letters/Digits combined: {re.findall(r'[a-zA-Z0-9]+', alphanumeric_str)}")

# Escaping Metacharacters: . ^ $ * + ? { } [ ] \ | ( )
# We must use \ to match them literally.
text = "The IP is [192.168.1.1]. Did it fail? (Yes/No)"
print(f"Literal bracket found: {bool(re.search(r'\[192', text))}")
print(f"Literal question mark found: {bool(re.search(r'\?', text))}")

# Complex Regex: Extracting an Email Address
contact = "Reach out to devops-team@company.com for support."
email_pattern = r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+"
print(f"Extracted Email: {re.findall(email_pattern, contact)}")

# 1.5 Other Search Methods
print("\n--- 1.5 Other Search Methods (match, fullmatch, finditer) ---")
test_str = "root logged in as root"

# re.match() ONLY checks the very beginning of the string (like an implicit ^)
is_start_root = re.match(r"root", test_str)
print(f"match() for 'root': {bool(is_start_root)}")

# re.fullmatch() MUST match the entire string from start to finish
is_full = re.fullmatch(r"root", test_str)
print(f"fullmatch() for 'root': {bool(is_full)} (Needs the whole string!)")

# re.finditer() returns an iterator of Match objects, giving us exact locations
for m in re.finditer(r"root", test_str):
    print(f"finditer() found '{m.group()}' at positions {m.start()} to {m.end()}")



print("\n" + "=" * 70)
print("SECTION 2: System Integration Basics (sys)")
print("-" * 70)

# 2.1 sys - Platform Detection
print("--- 2.1 sys: Platform Detection ---")
# The sys module allows Python to inspect interpreter state and host operating system flags.
# DevOps engineers use sys.platform to write conditional branching logic for multi-OS environments.
print(f"Platform: {sys.platform}")
# Output: 'linux' on Ubuntu/WSL, 'win32' on Windows, or 'darwin' on macOS

if sys.platform.startswith("linux"):
    print("Executing Linux-specific routines (e.g., systemd checks, journalctl).")
elif sys.platform == "win32":
    print("Executing Windows-specific routines (e.g., PowerShell commands, registry checks).")

# 2.2 sys - Command-Line Arguments (sys.argv)
print("\n--- 2.2 sys: Command-Line Arguments ---")
# sys.argv captures all command-line arguments passed to the script as a list of strings.
# Index 0 is always the script name itself, while index 1 and beyond contain user-supplied arguments.
print(f"Script Name (sys.argv[0]): {sys.argv[0]}")
print(f"Positional Arguments (sys.argv[1:]): {sys.argv[1:]}")

# Defensive argument checks verify that required parameters exist before executing critical operations
if len(sys.argv) > 1:
    target_node = sys.argv[1]
    print(f"Target node parameter provided: {target_node}")
else:
    print("No positional arguments passed. Running with default configuration.")

# 2.3 sys - Process Exit Codes (sys.exit)
print("\n--- 2.3 sys: Process Exit Codes ---")
# Process exit codes inform the calling shell or CI/CD runner whether an automation script succeeded or failed.
# Exit code 0 indicates success, while any non-zero integer (such as 1 or 2) communicates an error to the shell.
def check_server_health(status_code):
    if status_code != 200:
        # In a standalone script, sys.exit(1) terminates execution and sets shell status $? to 1
        return f"Service returned error {status_code}. sys.exit(1) would trigger failure."
    return f"Service healthy (HTTP {status_code}). sys.exit(0) signals clean completion."

print(check_server_health(200))
print(check_server_health(503))


print("\n" + "=" * 70)
print("SECTION 3: Functional Operations (lambda, map, filter)")
print("-" * 70)

# 3.1 Lambda Functions (Anonymous Single-Expression Functions)
print("--- 3.1 Lambda Functions ---")
# Lambda functions provide a concise syntax for defining small, throwaway functions in a single line.
# Syntax: lambda parameter1, parameter2: expression (the result is returned automatically without 'return').
format_server_tag = lambda host, env: f"{env.upper()}:{host.lower()}"
print(f"Formatted Server Tag: {format_server_tag('PROD-DB-01', 'production')}")

# Lambda functions are especially useful when formatting strings or performing simple calculations
calculate_ram_ratio = lambda used_mb, total_mb: round((used_mb / total_mb) * 100, 2)
print(f"Memory Usage Ratio: {calculate_ram_ratio(6144, 8192)}%")

# 3.2 The map() Function (Batch Transformations)
print("\n--- 3.2 The map() Function ---")
# map(function, iterable) applies a given function to every item in an iterable without explicit for-loops.
# It returns a map iterator, which can be converted to a list using list().
raw_ports = ["80", "443", "8080", "9090"]
# Converting a list of port strings into integers
int_ports = list(map(int, raw_ports))
print(f"Raw string ports: {raw_ports}")
print(f"Parsed integer ports: {int_ports}")

# Using map with a lambda function to normalize hostname strings
hostnames = ["  WEB-01.INTERNAL  ", "api-gw-02.internal  ", "  DB-MASTER.internal"]
clean_hosts = list(map(lambda h: h.strip().lower(), hostnames))
print(f"Cleaned hostnames: {clean_hosts}")

# 3.3 The filter() Function (Predicate Filtering)
print("\n--- 3.3 The filter() Function ---")
# filter(predicate_function, iterable) evaluates every element with a boolean function.
# Elements returning True are kept; elements returning False are discarded.
http_status_codes = [200, 201, 301, 400, 401, 403, 404, 500, 502, 503]

# Filtering for HTTP error statuses (4xx and 5xx)
is_error = lambda code: code >= 400
error_codes = list(filter(is_error, http_status_codes))
print(f"All Status Codes: {http_status_codes}")
print(f"Filtered Error Codes (>= 400): {error_codes}")

# Filtering active services by status flag
services = [
    {"name": "nginx", "active": True},
    {"name": "mysql", "active": False},
    {"name": "redis", "active": True},
    {"name": "docker", "active": False},
]
running_services = list(filter(lambda s: s["active"], services))
print(f"Running Services: {[s['name'] for s in running_services]}")

# 3.4 Combining Regex, Lambda, map(), and filter()
print("\n--- 3.4 Combining Regex, Lambda, map(), and filter() ---")
# In production log triage, combining regex with map and filter produces compact, expressive data pipelines.
# Here we filter an event log for error lines, and map the matches to extract sanitized alert summaries.
raw_telemetry = [
    "2026-10-06 12:00:01 [INFO] Node srv-01 health check passed (latency 5ms)",
    "2026-10-06 12:00:04 [ERROR] Database timeout at 192.168.1.50:5432 after 3000ms",
    "2026-10-06 12:00:09 [INFO] Node srv-02 health check passed (latency 8ms)",
    "2026-10-06 12:00:15 [ERROR] Unauthorized token access from 10.0.0.99:8080",
    "2026-10-06 12:00:22 [WARN] High memory on srv-03: 88% utilized",
]

# Step 1: Filter only log lines containing [ERROR]
error_lines = list(filter(lambda log: "[ERROR]" in log, raw_telemetry))
print(f"Filtered Error Lines ({len(error_lines)}):")
for err in error_lines:
    print(f" -> {err}")

# Step 2: Use map with re.sub() to redact IP addresses from the error lines for security
ip_regex = r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}"
sanitized_alerts = list(map(lambda log: re.sub(ip_regex, "[REDACTED_IP]", log), error_lines))
print("\nSanitized Alerts (PII Removed):")
for alert in sanitized_alerts:
    print(f" -> {alert}")



