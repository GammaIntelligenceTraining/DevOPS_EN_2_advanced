import os

print("=" * 70)
print("MODULE 4: Resilient Automation & Structured Data")
print("=" * 70)

print("\nSECTION 1: Defensive Exception Handling")
print("-" * 70)
# What is an Exception?
# An Exception is a Python object that represents an error during execution. 
# When a script encounters a critical issue (e.g., dividing by zero, reading a missing file), 
# it "raises" an Exception object. If your script doesn't "catch" this object, 
# the program halts immediately. In DevOps, a halted script means an incomplete deployment!
# 'try / except' blocks allow us to catch these objects and handle them gracefully.

# 1.1 Basic Try / Except (ValueError)
print("--- 1.1 Catching Value Errors ---")
dirty_telemetry = "CPU: 85.5%"
try:
    # This will fail because the string contains non-numeric characters
    cpu_float = float(dirty_telemetry)
    print(f"Parsed CPU: {cpu_float}")
except ValueError:
    print(f"[WARN] Could not convert '{dirty_telemetry}' to a float. Using fallback: 0.0")
    cpu_float = 0.0

# 1.2 Catching Missing Keys (KeyError)
print("\n--- 1.2 Catching Key Errors ---")
server_data = {"hostname": "web01", "ip": "10.0.0.5"}
try:
    # The key "os_version" does not exist!
    os_ver = server_data["os_version"]
    print(f"OS is: {os_ver}")
except KeyError:
    print("[WARN] 'os_version' key missing from server data.")

# 1.3 The 'else' Clause (Running when safe)
print("\n--- 1.3 The 'else' Clause ---")
# The 'else' block runs ONLY if the 'try' block succeeds without raising an exception.
try:
    port_int = int("80")
except ValueError:
    print("Failed to parse port.")
else:
    # This runs because int("80") succeeds!
    print(f"Successfully parsed port. Proceeding to bind to {port_int}...")

# 1.4 Catching ANY Error (The Exception Base Class)
print("\n--- 1.4 The Exception Base Class ---")
# 'Exception' is the master parent class of all standard errors.
# By catching 'Exception', you catch EVERYTHING (ValueError, KeyError, FileNotFoundError, etc.)
# We capture the object into a variable 'e' to see what actually went wrong.
try:
    # We are dividing by zero!
    calculation = 100 / 0
except Exception as e:
    # We catch the error, and print its details safely.
    print(f"[CRITICAL] A wild error appeared! Details: {e}")

# 1.5 Catching Multiple Errors
print("\n--- 1.5 Catching Multiple Errors ---")
# You can stack multiple except blocks to handle different errors in different ways.
def parse_config(config):
    try:
        # Might raise KeyError if "timeout" is missing
        timeout_str = config["timeout"]
        # Might raise ValueError if it isn't a number
        timeout_int = int(timeout_str)
        print(f"Timeout set to {timeout_int} seconds.")
    except KeyError:
        print("[WARN] Missing 'timeout' key. Defaulting to 30s.")
    except ValueError:
        print(f"[WARN] Invalid timeout value. Defaulting to 30s.")

parse_config({"host": "web01"})               # Triggers KeyError
parse_config({"timeout": "five_seconds"})     # Triggers ValueError
parse_config({"timeout": "60"})               # Succeeds

# 1.6 The Full Lifecycle (try / except / else / finally)
print("\n--- 1.6 The Full Exception Lifecycle ---")
def restart_service(service_name):
    print(f"Attempting to restart {service_name}...")
    try:
        if service_name == "crash_service":
            raise RuntimeError("The service daemon is unresponsive!") # Manually triggering an error
        print(f" -> {service_name} restarted successfully.")
    except Exception as e:
        # Catching the exception and viewing the message
        print(f" -> [ERROR] Restart failed: {e}")
    else:
        # Runs ONLY if NO error occurred
        print(" -> [SUCCESS] Verifying service status...")
    finally:
        # Runs ALWAYS (useful for closing network connections or files)
        print(" -> [CLEANUP] Disconnecting from server...")

restart_service("nginx")
print("")
restart_service("crash_service")


print("\n" + "=" * 70)
print("SECTION 2: File I/O (Input / Output)")
print("-" * 70)
file_path = "system_status.txt"

# 2.1 The Old Way (Without 'with')
print("--- 2.1 Manual File Management ---")
# If you don't use 'with', you MUST call .close() manually. 
# If the script crashes before .close() is called, the file remains locked!
manual_file = open(file_path, "w")
manual_file.write("Line 1: CPU OK\n")
manual_file.close() # CRITICAL!
print(f"File closed manually: {manual_file.closed}") # True

# 2.2 The Context Manager (with open)
print("\n--- 2.2 Context Managers (Safe Management) ---")
# 'with' guarantees the file closes the microsecond the block ends.
with open(file_path, "a") as f:
    print(f"Inside block, is file closed? {f.closed}") # False
    f.write("Line 2: RAM OK\n")
    f.write("Line 3: DISK OK\n")
print(f"Outside block, is file closed? {f.closed}") # True

# 2.3 Different Read Methods
print("\n--- 2.3 Read Methods ---")
with open(file_path, "r") as f:
    # 1. read() - Loads the ENTIRE file into one giant string.
    # DANGEROUS for huge log files (will consume all RAM).
    all_content = f.read()
    
with open(file_path, "r") as f:
    # 2. readline() - Reads exactly one line and pauses.
    first_line = f.readline().strip()
    
with open(file_path, "r") as f:
    # 3. readlines() - Reads the whole file and returns a LIST of lines.
    all_lines_list = f.readlines()
    
print(f"read() returned a {type(all_content)} of length {len(all_content)}")
print(f"readline() returned: '{first_line}'")
print(f"readlines() returned a {type(all_lines_list)} with {len(all_lines_list)} items")

# The BEST way to read huge files is to just loop over 'f':
# for line in f:
#     print(line)

# 2.4 Advanced Modes (x, rb, r+)
print("\n--- 2.4 Advanced Modes ---")
try:
    # 'x' (Exclusive creation): Creates a file. Crashes if it already exists!
    # Perfect for ensuring you don't accidentally overwrite a critical backup.
    with open("new_config.txt", "x") as f:
        f.write("Initial config.")
    print("Exclusive file created.")
except FileExistsError:
    print("[WARN] File already exists, 'x' mode blocked overwriting.")

# 'r+' (Read AND Write): Opens file without wiping it, allows reading and writing.
# 'rb' (Read Binary): Reads raw bytes instead of text. Used for images, PDFs, or encrypted data.
with open(file_path, "rb") as f:
    binary_data = f.read(4) # Read exactly 4 bytes
    print(f"Raw bytes: {binary_data}")


print("\n" + "=" * 70)
print("SECTION 3: Structured Data (JSON)")
print("-" * 70)
import json

# JSON (JavaScript Object Notation) is the universal language of APIs.
# It looks almost exactly like Python Dictionaries and Lists.

# 3.1 JSON Parsing (json.loads) - "Loads" converts a JSON String into a Python Dict
print("--- 3.1 Parsing JSON Strings (loads) ---")
api_response_string = '{"host": "db01", "uptime_days": 42, "is_active": true}'

parsed_dict = json.loads(api_response_string)
print(f"Parsed Type: {type(parsed_dict)}")
print(f"Extracted Hostname: {parsed_dict['host']}")

# 3.2 JSON Generation (json.dumps) - "Dumps" converts a Python Dict into a JSON String
print("\n--- 3.2 Generating JSON Strings (dumps) ---")
my_payload = {
    "target": "web02",
    "action": "reboot",
    "force": True,       # Python boolean
    "delay": None        # Python None
}

# The 'indent' parameter makes it human-readable (pretty-printing)
json_string = json.dumps(my_payload, indent=4)
print("Generated JSON Payload:")
print(json_string)

# 3.3 Writing JSON directly to a file (json.dump)
print("\n--- 3.3 Exporting JSON to a File (dump) ---")
json_file_path = "payload.json"
with open(json_file_path, "w") as f:
    json.dump(my_payload, f, indent=2)
print(f"Exported structured data to {json_file_path}")

# 3.4 Reading JSON directly from a file (json.load)
print("\n--- 3.4 Reading JSON from a File (load) ---")
# We can read the file we just created directly into a Python Dictionary
with open(json_file_path, "r") as f:
    imported_dict = json.load(f)

print(f"Imported Type: {type(imported_dict)}")
print(f"Imported Target: {imported_dict['target']}")

print("\\n" + "=" * 70)
print("SECTION 4: While Loops & Flow Control")
print("-" * 70)

# 4.1 Conditional while (Bounded Retries)
print("--- 4.1 Conditional while ---")
attempts = 0
max_attempts = 3

while attempts < max_attempts:
    attempts += 1
    print(f"Pinging server... (Attempt {attempts}/{max_attempts})")

print("Server is offline. Failing gracefully.")


# 4.2 Infinite Loops (while True), break, and continue
print("\\n--- 4.2 Infinite Loops, break, continue ---")
port = 8080
while True:
    port += 1
    
    if port == 8082:
        print("Port 8082 is blocked. Skipping (continue)...")
        continue  # Jumps back to the top immediately!
        
    print(f"Scanning port {port}...")
    
    if port == 8084:
        print("Target found! Stopping scan (break).")
        break  # Shuts down the entire loop!

print("\\n--- 4.3 DevOps Best Practices for while Loops ---")
print("1. THE ESCAPE HATCH: A while True loop must ALWAYS have a reachable break statement.")
print("2. CPU SPIKING: An empty or non-blocking while True loop will consume 100% of a CPU core.")

# --- Cleanup ---
# We clean up our temporary files so the workspace stays tidy.
import os
file_path = "system_status.txt"
json_file_path = "payload.json"
if os.path.exists(file_path):
    os.remove(file_path)
if os.path.exists(json_file_path):
    os.remove(json_file_path)
if os.path.exists("new_config.txt"):
    os.remove("new_config.txt")
