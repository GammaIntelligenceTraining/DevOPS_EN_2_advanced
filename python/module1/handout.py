#!/usr/bin/env python3
"""
Module 1: Python Fundamentals for DevOps - Student Handout

This executable handout covers fundamental syntax, primitive types, explicit type
conversion, special escape characters, string indexing and slicing, essential string
methods, string membership, interactive operator input, arithmetic capacity math,
augmented assignments (+=, -=), and f-string formatting.

Topics covered:
1. Primitive data types (int, float, str, bool) and type inspection with type()
2. Explicit type conversion: int(), float(), str(), bool() and falsy values
3. Special string characters, escape sequences (\\n, \\t), raw strings, and multiline text
4. String indexing vs slicing, boundary safety rules, and string membership ('in')
5. Essential string methods for log cleaning (.strip, .split, .replace, .count)
6. Interactive operator input via input() with fallback defaults
7. Arithmetic capacity operations (+, -, *, /, //, %, **) and augmented assignments (+=, -=)
8. Modern f-strings with precision specifiers and column alignment

Execution:
    Run directly in VS Code by clicking the Play button, or run in the integrated terminal:
    - Windows (PowerShell): python handout.py
    - macOS (Terminal)    : python3 handout.py
"""

# ==============================================================================
# 1. Primitive Data Types & Type Inspection
# ==============================================================================
# In systems automation, configuration settings, socket identifiers, metrics,
# and states map to four fundamental primitive types:
# - int:   Whole numbers (ports, PIDs, HTTP status codes, byte counters)
# - float: Decimal numbers (CPU load averages, memory ratios, latency in ms)
# - str:   Textual data (hostnames, IP addresses, log lines, systemd unit names)
# - bool:  Binary states (True/False: is_running, firewall_enabled)

print("=" * 70)
print("SECTION 1: Primitive Data Types and Variable Assignment")
print("=" * 70)

ssh_port = 22                         # int: network port number
target_host = "web-prod-01.internal"  # str: Fully Qualified Domain Name
cpu_load_1m = 1.85                    # float: 1-minute load average
is_service_active = True              # bool: service operational status

# Inspect runtime types using the type() built-in function
print("Variable 'ssh_port':", ssh_port, "| Type:", type(ssh_port))
print("Variable 'target_host':", target_host, "| Type:", type(target_host))
print("Variable 'cpu_load_1m':", cpu_load_1m, "| Type:", type(cpu_load_1m))
print("Variable 'is_service_active':", is_service_active, "| Type:", type(is_service_active))

# Dynamic vs. Strong Typing:
# Variables can be reassigned to different types at runtime (dynamic typing).
# However, Python NEVER implicitly converts mismatched types across operations (strong typing).
# Uncomment the following line to see Python raise a TypeError at runtime:
# bad_concat = ssh_port + " is open"
# Expected error: TypeError: unsupported operand type(s) for +: 'int' and 'str'


# ==============================================================================
# 2. Explicit Type Conversion (Casting) & Falsy Values
# ==============================================================================
# Input read from terminals, files, or CLI arguments is always str. You must
# explicitly convert strings to numeric or boolean types using int(), float(), etc.

print("\n" + "=" * 70)
print("SECTION 2: Explicit Type Conversion (Casting) & Falsy Values")
print("=" * 70)

raw_port = "8080"
raw_ratio = "0.75"
raw_core_count = 16

# Explicit conversion to numeric types
port_number = int(raw_port)
threshold_ratio = float(raw_ratio)
core_string = str(raw_core_count)

print("Converted int  :", port_number, "| Type:", type(port_number))
print("Converted float:", threshold_ratio, "| Type:", type(threshold_ratio))
print("Converted str  :", core_string, "| Type:", type(core_string))

# Direct conversion pitfall: int() cannot directly parse decimal strings.
# Uncomment the following line to see Python raise a ValueError:
# bad_int_parse = int("80.5")
# Expected error: ValueError: invalid literal for int() with base 10: '80.5'
# Correct fix: Parse to float first, then int: int(float("80.5")) -> 80

# Truthiness & Falsy Values:
# In Python, the following values evaluate to False (falsy) when converted via bool():
# - Constants: None, False
# - Numeric zeros: 0, 0.0
# - Empty strings: ""
# All other values evaluate to True (truthy).
print("Falsy test - bool(''):", bool(""))          # Empty string is False
print("Falsy test - bool(0):", bool(0))            # Zero integer is False
print("Falsy test - bool(0.0):", bool(0.0))        # Zero float is False
print("Truthy test - bool('0'):", bool("0"))        # Non-empty string "0" is True!
print("Truthy test - bool('False'):", bool("False"))# Non-empty string "False" is True!
print("Truthy test - bool(100):", bool(100))        # Non-zero number is True


# ==============================================================================
# 3. Special String Characters, Escape Sequences & Raw Strings
# ==============================================================================
# Special characters are represented using a backslash (\) escape prefix:
# - \n : Newline (line break)
# - \t : Horizontal tab (indentation, TSV parsing)
# - \' : Single quote literal
# - \" : Double quote literal
# - \\ : Literal backslash
#
# Raw strings (prefixed with r"...") treat backslashes as literal characters,
# preventing Python from interpreting escape sequences. Raw strings are essential
# for regex patterns and Windows filesystem paths.

print("\n" + "=" * 70)
print("SECTION 3: Special String Characters, Escapes, and Raw Strings")
print("=" * 70)

# Newline and tab escape characters
server_banner = "SYSTEM STATUS:\n\tCPU:\t84.5%\n\tRAM:\t12.0 GiB\n\tSTATE:\tONLINE"
print("Formatted Banner using \\n and \\t:")
print(server_banner)

# Literal quotes and backslashes
command_snippet = "Executing: sudo -u \"deploy_bot\" /bin/bash -c 'systemctl restart nginx'"
windows_path = "C:\\Users\\Administrator\\AppData\\Local\\Temp\\deploy.log"
print("\nEscaped quotes and path:")
print(command_snippet)
print(windows_path)

# Raw string demonstration (note prefix 'r')
raw_regex_pattern = r"^192\.168\.\d{1,3}\.\d{1,3}$"
print("Raw string regex pattern:", raw_regex_pattern)

# Multiline strings using triple quotes (""" or ''')
multiline_config = """[server]
bind_address = 0.0.0.0
port = 8080
workers = 4"""
print("\nMultiline string:")
print(multiline_config)


# ==============================================================================
# 4. String Indexing, Slicing & Membership ('in')
# ==============================================================================
# Strings are ordered sequences of characters. Each character has a specific index:
# - Positive indexing starts at 0 (from the beginning).
# - Negative indexing starts at -1 (from the end).
#
# Slicing extracts a substring using the syntax: string[start:stop:step]
# - start: starting index (inclusive)
# - stop:  stopping index (exclusive)
# - step:  optional stride (default is 1)

print("\n" + "=" * 70)
print("SECTION 4: String Indexing, Slicing & Membership ('in')")
print("=" * 70)

hostname = "srv-us-east-web-04"
# Index mapping:
#  s  r  v  -  u  s  -  e  a  s  t  -  w  e  b  -  0  4
#  0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17
# -18                                              -2 -1

# 1. Single character indexing
first_char = hostname[0]     # 's'
last_char = hostname[-1]     # '4'
print(f"Hostname: {hostname}")
print(f"First character: '{first_char}' | Last character: '{last_char}'")

# Direct indexing out-of-bounds raises IndexError!
# Uncomment the following line to see Python crash:
# bad_index = hostname[999]
# Expected error: IndexError: string index out of range

# 2. Slicing substrings
server_type = hostname[0:3]   # characters at index 0, 1, 2 -> 'srv'
region = hostname[4:11]       # characters from index 4 up to 11 -> 'us-east'
role = hostname[12:15]        # characters from index 12 up to 15 -> 'web'
instance_id = hostname[-2:]   # last 2 characters -> '04'

print(f"Extracted Type   : '{server_type}'")
print(f"Extracted Region : '{region}'")
print(f"Extracted Role   : '{role}'")
print(f"Extracted ID     : '{instance_id}'")

# 3. Slicing Out-of-Bounds Safety Rule:
# Unlike direct indexing, slicing past the end of a string NEVER raises an IndexError!
# Python gracefully clamps the slice to the end of the string.
safe_tail = hostname[12:999]
print("Safe out-of-bounds slice ([12:999]):", safe_tail)

# 4. Slicing shortcuts and stride
print("Prefix up to index 7 ([:7]):", hostname[:7])
print("Suffix from index 12 ([12:]):", hostname[12:])
print("Reversed string ([::-1]):", hostname[::-1])

# 5. String Membership with 'in' and 'not in':
# Checks if a substring exists within a target string.
has_web_role = "web" in hostname
is_legacy = "legacy" not in hostname
print("Contains 'web' role ('web' in hostname):", has_web_role)
print("Is not legacy ('legacy' not in hostname):", is_legacy)


# ==============================================================================
# 5. Essential String Methods for Telemetry & Log Sanitization
# ==============================================================================
# Python strings are immutable: string methods return a newly transformed string.

print("\n" + "=" * 70)
print("SECTION 5: String Methods for Systems Automation")
print("=" * 70)

# 1. Whitespace stripping: .strip(), .lstrip(), .rstrip()
dirty_log = "  \n  [AUTH_FAIL] Access denied for user admin from 10.0.0.99 \t\n"
clean_log = dirty_log.strip()
print("Raw log length  :", len(dirty_log))
print("Clean log length:", len(clean_log))
print("Cleaned text    :", clean_log)

# 2. Case normalization: .lower(), .upper()
env_var = "Production_East"
print("Normalized lowercase:", env_var.lower())
print("Normalized uppercase:", env_var.upper())

# 3. Prefix and suffix checking: .startswith(), .endswith()
is_auth_failure = clean_log.startswith("[AUTH_FAIL]")
is_log_file = "syslog.2.gz".endswith(".gz")
print("Log line is auth failure:", is_auth_failure)
print("File has .gz extension  :", is_log_file)

# 4. Replacement: .replace()
legacy_url = "http://internal-vault:8200/v1/secret"
secure_url = legacy_url.replace("http://", "https://")
print("Secured Vault URL       :", secure_url)

# 5. Splitting and endpoint unpacking teaser: .split()
# Note: .split() returns a list (covered deeply in Module 2).
# When the exact token count is known, we can unpack directly into discrete variables.
endpoint = "10.0.12.44:9092"
host_ip, port_str = endpoint.split(":")
target_port = int(port_str)
print(f"Unpacked Endpoint       : Host={host_ip}, Port={target_port} (Type: {type(target_port)})")

# Counting occurrences: .count()
log_batch = "INFO: start. WARN: disk 82%. WARN: cpu 88%. INFO: done."
warn_count = log_batch.count("WARN")
print("Warning count in batch  :", warn_count)


# ==============================================================================
# 6. Interactive Operator Prompts with input() & Fallback Defaults
# ==============================================================================
# The input() function pauses script execution and reads a line from stdin.
# It always returns a string.

print("\n" + "=" * 70)
print("SECTION 6: Interactive Operator Input Simulation")
print("=" * 70)

# Simulating user pressing Enter without typing (empty string "")
simulated_user_entry = ""

# The boolean 'or' fallback pattern:
# If simulated_user_entry is empty (""), it is falsy.
# Python evaluates and returns the right-hand operand ("8080").
configured_port_str = simulated_user_entry or "8080"
configured_port = int(configured_port_str)
print("Operator input received :", repr(simulated_user_entry))
print("Effective Port Fallback :", configured_port, "| Type:", type(configured_port))


# ==============================================================================
# 7. Arithmetic Operations, Capacity Math & Augmented Assignments (+=, -=)
# ==============================================================================
# Arithmetic operators calculate storage limits, worker allocations, and throughput:
#   +   Addition
#   -   Subtraction
#   *   Multiplication
#   /   True Division (always returns float)
#   //  Floor Division (rounds down to nearest integer)
#   %   Modulo (returns remainder of division)
#   **  Exponentiation (power)
#
# Augmented assignments update a variable in-place:
#   remaining -= used   (equivalent to: remaining = remaining - used)
#   counter += 1        (equivalent to: counter = counter + 1)

print("\n" + "=" * 70)
print("SECTION 7: Arithmetic Operations, Capacity Math & Augmented Assignments")
print("=" * 70)

# Memory capacity allocation scenario:
total_ram_bytes = 34359738368   # 32 GiB in bytes
used_ram_bytes = 25769803776    # 24 GiB in bytes

# Binary conversion constant (1 GiB = 1024^3 bytes = 1,073,741,824 bytes)
bytes_per_gib = 1024 ** 3

total_ram_gib = total_ram_bytes / bytes_per_gib
used_ram_gib = used_ram_bytes / bytes_per_gib
free_ram_gib = total_ram_gib - used_ram_gib
ram_utilization_percent = (used_ram_bytes / total_ram_bytes) * 100

print(f"Total RAM (GiB): {total_ram_gib:.2f}")
print(f"Used RAM (GiB) : {used_ram_gib:.2f}")
print(f"Free RAM (GiB) : {free_ram_gib:.2f}")
print(f"RAM Utilization: {ram_utilization_percent:.2f}%")

# Pod capacity scheduling using floor division (//) and modulo (%):
pod_ram_requirement_gib = 2.5
max_deployable_pods = int(free_ram_gib // pod_ram_requirement_gib)
remaining_headroom_gib = free_ram_gib % pod_ram_requirement_gib

print(f"Pod Requirement : {pod_ram_requirement_gib:.2f} GiB")
print(f"Max Deployable  : {max_deployable_pods} pods (via //)")
print(f"RAM Headroom    : {remaining_headroom_gib:.2f} GiB (via %)")

# Augmented assignments demonstration:
# Simulating deployment of 1 pod deducting from available memory
allocated_pool_gib = free_ram_gib
allocated_pool_gib -= pod_ram_requirement_gib
print(f"Headroom after scheduling 1 pod (-=): {allocated_pool_gib:.2f} GiB")

# Simulating event retry increment
retry_count = 0
retry_count += 1
print("Retry counter after increment (+=):", retry_count)


# ==============================================================================
# 8. Modern f-String Formatting & Output Alignment
# ==============================================================================
# F-strings support variable interpolation, float precision, and column padding.

print("\n" + "=" * 70)
print("SECTION 8: Modern f-String Formatting")
print("=" * 70)

domain = "cloud.internal"
fqdn = f"{hostname}.{domain}"
print(f"Constructed FQDN: {fqdn}")

# Tabular column formatting:
# <18 left-aligns in an 18-character field
# >10 right-aligns in a 10-character field
print("\n" + f"{'SERVER HOSTNAME':<22} {'REGION':<10} {'ROLE':<8} {'RAM (GiB)':>10}")
print("-" * 54)
print(f"{'srv-us-east-web-01':<22} {'us-east':<10} {'web':<8} {32.0:>10.2f}")
print(f"{'srv-us-east-web-02':<22} {'us-east':<10} {'web':<8} {32.0:>10.2f}")
print(f"{'srv-eu-west-db-01':<22} {'eu-west':<10} {'db':<8} {64.0:>10.2f}")

print("\n" + "=" * 70)
print("Handout walkthrough completed successfully.")
print("=" * 70)
