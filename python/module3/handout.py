#!/usr/bin/env python3
"""
Module 3: Advanced Collections, Loops & Functions - Student Handout

This executable handout covers Dictionaries, Tuples, Sets, and Functions.

Topics covered:
1. Dictionaries: Key-value mapping, safe parsing with .get(), and .items() iteration.
2. Tuples & Sets: Immutable sequences, coordinate pairs, and mathematical deduplication.
3. Functions & Scope: Defining reusable automation blocks with def and type hints.
4. Synthesis: An end-to-end telemetry evaluation loop.

Execution:
    Run directly in VS Code by clicking the Play button, or run in the integrated terminal:
    - Windows (PowerShell): python handout.py
    - macOS (Terminal)    : python3 handout.py
"""

print("\n" + "=" * 70)
print("SECTION 1: Dictionaries - Key/Value Telemetry Mapping")
print("=" * 70)
# Dictionaries map 'keys' to 'values'. They are the Python equivalent of JSON.
server_node = {
    "hostname": "web-prod-01",
    "ip_addr": "10.0.1.50",
    "role": "frontend",
    "cpu_pct": 82.5,
    "active": True
}

# 1.1 Dictionary Key Datatypes (Immutability)
# Keys MUST be immutable types (strings, integers, floats, or tuples).
# Lists or other dictionaries CANNOT be keys because they can change.
valid_dict = {
    80: "HTTP",
    443: "HTTPS",
    ("10.0.1.1", 22): "SSH_Socket"  # Tuple as a key!
}
print(f"Port 80 maps to: {valid_dict[80]}")

# 1.2 Accessing, Mutating & Safely Parsing (.get)
server_node["cpu_pct"] = 91.0  # Mutate in-place
server_node["ram_pct"] = 65.0  # Add a new key
# Direct lookup server_node["missing_key"] causes a fatal KeyError!
# .get() returns None (or a fallback) if the key doesn't exist.
print("Safe uptime :", server_node.get("uptime_days", 0), "days")

# 1.3 Removing Items (.pop vs del)
# .pop() removes the key and RETURNS its value.
removed_role = server_node.pop("role")
print(f"Removed role: {removed_role}")
# del simply deletes it (throws KeyError if missing)
del server_node["active"]

# 1.4 Dictionary Methods & for Loops (.keys, .values, .items)
print("\n--- .keys() Iteration ---")
for k in server_node.keys():
    print(f"Key found: {k}")

print("\n--- .values() Iteration ---")
for v in server_node.values():
    print(f"Value found: {v}")

print("\n--- .items() Iteration (Most Common) ---")
for key, value in server_node.items():
    print(f"  {key:<12} -> {value}")

# 1.5 Nested Dictionaries
# Real-world JSON often contains dictionaries inside dictionaries.
infrastructure = {
    "us-east": {
        "web": "10.0.1.10",
        "db": "10.0.1.20"
    },
    "eu-west": {
        "web": "10.1.1.10",
        "db": "10.1.1.20"
    }
}
# Chaining keys to dig into nested structures
eu_db_ip = infrastructure["eu-west"]["db"]
print(f"\nEU-West Database IP: {eu_db_ip}")

# 1.6 DevOps Best Practices for Dictionaries
print("\n--- 1.6 Best Practices ---")
print("1. Never trust external JSON. Always use .get() to prevent fatal script crashes.")
print("2. Do not delete keys while looping over a dictionary (RuntimeError).")
print("3. Keep keys consistent (e.g., use snake_case strings, not mixed types).")


print("\n" + "=" * 70)
print("SECTION 2: Tuples & Sets - Immutable Endpoints & Deduplication")
print("=" * 70)
# 2.1 Tuples
# Tuples are lists that CANNOT be changed (immutable). Perfect for fixed pairs like sockets.
db_socket = ("10.0.1.200", 5432)
# db_socket[1] = 3306  # FATAL TypeError: 'tuple' object does not support item assignment

# Implicit Tuple Packing & Unpacking
ip, port = db_socket   # Unpacking a tuple into separate variables
a = 1, 2, 3            # Implicit Packing: Python evaluates the right side as a tuple (1, 2, 3)
print(f"Implicitly packed tuple 'a': {a}")

# The Single Element Tuple Trap:
# You MUST include a trailing comma for a 1-element tuple, otherwise Python thinks it's math parens!
not_a_tuple = ("10.0.1.1")     # Type: str
real_tuple = ("10.0.1.1",)     # Type: tuple
print(f"real_tuple type: {type(real_tuple)}")

# Tuple Concatenation (Creates a NEW tuple, doesn't mutate)
web_ports = (80, 443)
db_ports = (5432, 3306)
all_ports = web_ports + db_ports
print(f"Concatenated tuple: {all_ports}")

# Type Conversion and Memory Identity (id)
# id() shows the underlying memory address of an object.
immutable_pair = ("admin", "guest")
print(f"Tuple ID : {id(immutable_pair)}")

# If we convert it to a list to mutate it, it becomes an entirely new object in memory!
mutable_list = list(immutable_pair)
print(f"List ID  : {id(mutable_list)}")  # Completely different memory address
mutable_list.append("operator")
print(f"Converted List: {mutable_list}")

# 2.2 Sets - Fast Hash-Based Lookups & Deduplication
# WHY SETS? Lists are slow for checking membership (O(n)). Sets use Hash Tables, 
# making lookups lightning fast (O(1)). They also mathematically prevent duplicates.

raw_ips = ["192.168.1.1", "10.0.0.5", "192.168.1.1", "10.0.0.5", "172.16.0.1"]
unique_ips = set(raw_ips)

# Sets are UNORDERED. The order you print them rarely matches the order you created them.
print(f"Raw IPs list (len={len(raw_ips)}): {raw_ips}")
print(f"Unique IPs set (len={len(unique_ips)}): {unique_ips}") # Order is guaranteed to be random

print("\n--- Set Specific Methods ---")
admin_users = {"root", "sysadmin"}

# Add a single item
admin_users.add("netadmin")

# Update adds multiple items (like list.extend)
admin_users.update(["dbadmin", "secadmin"])

# Removal (.discard vs .remove)
admin_users.discard("missing_user") # Fails safely (does nothing)
# admin_users.remove("missing_user") # FATAL KeyError if the item doesn't exist!

# Pop removes a RANDOM element (because sets are unordered!)
randomly_removed = admin_users.pop()
print(f"Popped user: {randomly_removed}")

# Clear wipes the entire set
admin_users.clear()
print(f"Cleared set: {admin_users}")

# Set Algebra (Math) - Operators vs Named Methods
prod_servers = {"web01", "web02", "db01"}
patch_queue = {"web02", "db01", "cache01"}

print("\n--- Set Algebra ---")
# 1. Intersection (Items in BOTH sets)
print("Intersection (&)      :", prod_servers & patch_queue)
print("Intersection (method) :", prod_servers.intersection(patch_queue))

# 2. Union (ALL items combined, duplicates removed)
print("Union (|)             :", prod_servers | patch_queue)
print("Union (method)        :", prod_servers.union(patch_queue))

# 3. Difference (Items in A but NOT in B)
print("Difference (-)        :", prod_servers - patch_queue)
print("Difference (method)   :", prod_servers.difference(patch_queue))

# 4. Symmetric Difference (Items in ONE set, but NOT both)
print("Sym Difference (^)    :", prod_servers ^ patch_queue)
print("Sym Diff (method)     :", prod_servers.symmetric_difference(patch_queue))

print("\n--- Set Comparisons ---")
subnet_a = {"10.0.0.1", "10.0.0.2"}
subnet_b = {"10.0.0.1", "10.0.0.2", "10.0.0.3"}
isolated = {"192.168.1.1"}

print(f"Is A a subset of B?       {subnet_a.issubset(subnet_b)}")
print(f"Is B a superset of A?     {subnet_b.issuperset(subnet_a)}")
print(f"Are A and Isolated disjoint? {subnet_a.isdisjoint(isolated)}")

# Adding to an empty set
blocked_ips = set() # Note: {} creates an empty DICTIONARY, not a set!
blocked_ips.add("1.1.1.1")


print("\n" + "=" * 70)
print("SECTION 3: Functions (Step-by-Step)")
print("=" * 70)
# Functions encapsulate automation blocks so you don't repeat code (DRY principle).

print("\n--- 3.1 No Arguments, No Return ---")
# The simplest function. It just executes a block of code.
def print_banner():
    print("---------------------------------")
    print("   SERVER DIAGNOSTICS V1.0       ")
    print("---------------------------------")

print_banner()  # Execution behavior: Prints text directly to the screen.

print("\n--- 3.2 Adding a Return Value ---")
# Instead of printing, the function hands data BACK to the caller.
def get_system_status():
    # Imagine this checks a real server...
    return "ONLINE"

current_status = get_system_status()
print(f"The system is currently: {current_status}")

print("\n--- 3.3 Required Positional Arguments ---")
# Arguments pass data INTO the function. Positional arguments are mandatory.
def scan_port(ip_address, port_number):
    print(f"Scanning {ip_address} on port {port_number}...")

scan_port("10.0.0.5", 443)  # Order matters!

print("\n--- 3.4 Default (Optional) Arguments ---")
# Default arguments provide a fallback if the caller omits them.
def check_disk(disk_name, threshold_pct=80.0):
    print(f"Checking {disk_name} (Alert Threshold: {threshold_pct}%)")

check_disk("/var/log")          # Uses default 80.0
check_disk("/database", 95.5)   # Overrides default with 95.5

print("\n--- 3.5 Variable Arguments (*args & **kwargs) ---")
# *args allows passing ANY number of positional arguments (packs them into a Tuple).
def block_ips(*ips_to_block):
    print(f"Blocking {len(ips_to_block)} IPs: {ips_to_block}")

block_ips("1.1.1.1")
block_ips("8.8.8.8", "9.9.9.9", "4.4.4.4")

# **kwargs allows passing ANY number of named arguments (packs them into a Dictionary).
def configure_server(**settings):
    print(f"Applying settings: {settings}")

configure_server(hostname="web01", os="ubuntu", ram_gb=16)

print("\n--- 3.6 Visibility Areas (Scope) ---")
GLOBAL_CONFIG = "prod-env" # Global scope: Visible everywhere

def demo_scope():
    local_token = "abc-123" # Local scope: ONLY exists inside this function
    print(f"Inside function: Can see global config -> {GLOBAL_CONFIG}")
    print(f"Inside function: Can see local token -> {local_token}")

demo_scope()
# print(local_token) # Fatal NameError: 'local_token' is not defined here!

print("\n--- 3.7 Function Calling a Global Function ---")
# Functions can call other functions to build complex, modular pipelines.
def fetch_logs():
    return ["log1", "log2"]

def orchestrate_backup():
    print("Starting orchestration...")
    logs = fetch_logs()  # Calling the globally available function
    print(f"Backed up {len(logs)} logs.")

orchestrate_backup()

print("\n--- 3.8 Callbacks (Functions as Parameters) ---")
# You can pass a function into another function as an argument!
def on_success():
    print("Callback triggered: The job finished successfully!")

def on_failure():
    print("Callback triggered: The job crashed! Sending Slack alert.")

def execute_job(job_name, callback_function):
    print(f"Running job: {job_name}...")
    # Pretend the job finishes here...
    callback_function()  # We execute whatever function was passed in!

execute_job("Database Backup", on_success)
execute_job("Cache Purge", on_failure)

print("\n--- 3.9 Complex DevOps Function: The Triage Engine ---")
# Bringing it all together: Positional Args, Default Args, Returns, and Callbacks!
def quarantine_node(ip_address):
    print(f" -> [FIREWALL] Executing UFW block on {ip_address}...")

def audit_server(ip, cpu_load, threshold=90.0, on_critical_callback=None):
    """Audits a server and triggers an emergency callback if it breaches threshold."""
    print(f"Auditing {ip} (Current Load: {cpu_load}%)")
    
    if cpu_load >= threshold:
        print(f" -> [ALERT] {ip} breached {threshold}% threshold!")
        if on_critical_callback:
            on_critical_callback(ip)  # Trigger the callback!
        return False # Audit failed
        
    return True # Audit passed

# Test 1: Healthy Server (Overrides default threshold to 80.0)
audit_server("10.1.1.5", cpu_load=75.0, threshold=80.0)

# Test 2: Unhealthy Server (Uses default 90.0 threshold, triggers callback)
audit_server("10.1.1.9", cpu_load=99.9, on_critical_callback=quarantine_node)


print("\n" + "=" * 70)
print("SECTION 4: Synthesis - List Iteration & Evaluation")
print("=" * 70)

def triage_event(event: dict) -> tuple:
    """Parses event dictionary and returns (is_critical, endpoint_tuple)."""
    ip = event.get("ip", "unknown")
    port = event.get("port", 0)
    err_code = event.get("error_code", 200)
    
    is_critical = (err_code >= 500)
    endpoint = (ip, port)
    return is_critical, endpoint

event_log = [
    {"ip": "10.0.0.5", "port": 80, "error_code": 200},
    {"ip": "10.0.0.9", "port": 443, "error_code": 503},
    {"ip": "10.0.0.9", "port": 443, "error_code": 503},
]

critical_endpoints = set()

print("Analyzing event log...")
for current_event in event_log:
    critical, target = triage_event(current_event)
    
    if critical:
        critical_endpoints.add(target)

print(f"Analysis complete. Unique critical endpoints requiring attention:")
for endpoint in critical_endpoints:
    print(f" -> {endpoint}")

