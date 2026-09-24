#!/usr/bin/env python3
"""
Module 1 Homework: Server Telemetry Ingestion, Hostname Slicing & Capacity Calculator

Overview:
In systems engineering, telemetry feeds often provide raw server metrics as text.
In this assignment, you will write a complete Python script that cleans raw strings,
slices metadata from hostnames, converts text metrics to numerical types, prompts
for operator input with fallback defaults, performs capacity calculations, and
constructs a clean, multi-line formatted f-string report.

Notice:
Do not use .split() or collections (lists/dictionaries) in this assignment.
All string extraction must be performed using string slicing [start:stop] and string methods.

Execution:
    Run directly in VS Code by clicking the Play button, or run in the integrated terminal:
    - Windows (PowerShell): python homework.py
    - macOS (Terminal)    : python3 homework.py
"""

# ==============================================================================
# Provided Raw Telemetry Data (Do not modify these input variables)
# ==============================================================================
raw_hostname = "\t  srv-prd-web-04  \n"
raw_ip = "192.168.10.45"
raw_port = "8080"
raw_total_ram = "34359738368"    # Total RAM in bytes (32 GiB)
raw_used_ram = "25769803776"     # Consumed RAM in bytes (24 GiB)
raw_cores = "16"                 # Total hardware CPU cores
raw_load_1m = "12.8"             # 1-minute CPU load average


# ==============================================================================
# TASK 1: String Sanitization & Slicing Metadata Extraction
# ==============================================================================
# 1. Sanitize 'raw_hostname' by removing leading/trailing whitespace, tabs,
#    and newline characters using the .strip() method. Store the result in 'hostname'.
#
# 2. Extract metadata components from 'hostname' (which has the structure 'srv-prd-web-04')
#    using string slicing [start:stop] and negative indexing:
#    - 'server_prefix'    : First 3 characters ('srv') -> slice [0:3]
#    - 'environment_tier' : 3-character tier ('prd')   -> slice [4:7]
#    - 'service_role'     : 3-character role ('web')   -> slice [8:11]
#    - 'node_id'          : Last 2 characters ('04')   -> slice [-2:]
#
# 3. Normalize 'environment_tier' to uppercase using .upper() (producing 'PRD').
#
# Code Example:
#   sample = "app-dev-01"
#   env = sample[4:7].upper()  # Produces 'DEV'

# TODO: Complete Task 1 below
hostname = ""
server_prefix = ""
environment_tier = ""
service_role = ""
node_id = ""


# ==============================================================================
# TASK 2: Explicit Type Conversion (Casting) & Operator Input with Fallback
# ==============================================================================
# 1. Convert the raw telemetry strings to appropriate numeric types:
#    - Convert 'raw_total_ram' to an integer using int()  -> store in 'total_ram_bytes'
#    - Convert 'raw_used_ram' to an integer using int()   -> store in 'used_ram_bytes'
#    - Convert 'raw_cores' to an integer using int()      -> store in 'total_cpu_cores'
#    - Convert 'raw_load_1m' to a float using float()     -> store in 'used_cpu_cores'
#    - Convert 'raw_port' to an integer using int()       -> store in 'port_number'
#
# 2. Prompt the operator for pod RAM requirements using input().
#    If the operator presses Enter without typing an input, use the boolean 'or'
#    operator to fall back to the default value "2.5".
#    Convert the chosen value to a float and store it in 'pod_ram_gib'.
#
# Code Example:
#   raw_val = input("Enter limit [default: 10]: ").strip()
#   limit = float(raw_val or "10")

# TODO: Complete Task 2 below
total_ram_bytes = 0
used_ram_bytes = 0
total_cpu_cores = 0
used_cpu_cores = 0.0
port_number = 0

# Interactive prompt with default fallback
raw_pod_input = input("Enter pod RAM requirement in GiB [default: 2.5]: ").strip()
pod_ram_gib = float(raw_pod_input or "2.5")


# ==============================================================================
# TASK 3: Systems Capacity Arithmetic
# ==============================================================================
# 1. Define the binary constant for bytes per GiB using the exponentiation operator (**):
#    bytes_per_gib = 1024 ** 3
#
# 2. Convert total and used RAM from bytes to GiB using floating-point division (/):
#    - total_ram_gib = total_ram_bytes / bytes_per_gib
#    - used_ram_gib = used_ram_bytes / bytes_per_gib
#    - free_ram_gib = total_ram_gib - used_ram_gib
#    - ram_usage_pct = (used_ram_bytes / total_ram_bytes) * 100
#
# 3. Calculate CPU utilization metrics:
#    - free_cpu_cores = total_cpu_cores - used_cpu_cores
#    - cpu_usage_pct = (used_cpu_cores / total_cpu_cores) * 100
#
# 4. Calculate worker pod scheduling capacity:
#    - 'max_pods': How many full pods can fit into free_ram_gib?
#      Use floor division (//) to calculate the integer pod count.
#    - 'remaining_headroom_gib': How much RAM remains unallocated after scheduling max_pods?
#      Use modulo (%) to calculate the remainder.
#
# Code Example:
#    capacity = free_ram // pod_size
#    leftover = free_ram % pod_size

# TODO: Complete Task 3 below
bytes_per_gib = 1024 ** 3
total_ram_gib = 0.0
used_ram_gib = 0.0
free_ram_gib = 0.0
ram_usage_pct = 0.0

free_cpu_cores = 0.0
cpu_usage_pct = 0.0

max_pods = 0
remaining_headroom_gib = 0.0


# ==============================================================================
# TASK 4: Building the Formatted f-String Report
# ==============================================================================
# Construct a multi-line formatted f-string named 'report' and print it to standard output.
#
# Formatting Requirements:
# - All GiB numbers and percentages must be formatted to two decimal places (:.2f).
# - Core counts for used/free must be formatted to two decimal places (:.2f).
# - Hardware total cores and max pods must be displayed as whole numbers.
# - Use the extracted metadata and calculated values.
#
# Expected Report Format:
# ======================================================================
# HOST ASSESSMENT REPORT: srv-prd-web-04
# ======================================================================
# Infrastructure Tier : PRD (Node ID: 04)
# Service Role        : web (Type: srv)
# Network Endpoint    : 192.168.10.45:8080
# 
# --- COMPUTE METRICS ---
# CPU Capacity        : 16 Cores Total | 12.80 Cores Used | 3.20 Cores Free
# CPU Utilization     : 80.00%
# 
# RAM Capacity        : 32.00 GiB Total | 24.00 GiB Used | 8.00 GiB Free
# RAM Utilization     : 75.00%
# 
# --- POD CAPACITY SCHEDULING ---
# Pod Requirement     : 2.50 GiB RAM
# Max Deployable      : 3 Pods
# Remaining Headroom  : 0.50 GiB RAM
# ======================================================================

# TODO: Construct the 'report' f-string and print it
report = f"""======================================================================
HOST ASSESSMENT REPORT: {hostname}
======================================================================
Infrastructure Tier : {environment_tier} (Node ID: {node_id})
Service Role        : {service_role} (Type: {server_prefix})
Network Endpoint    : {raw_ip}:{port_number}

--- COMPUTE METRICS ---
CPU Capacity        : {total_cpu_cores} Cores Total | {used_cpu_cores:.2f} Cores Used | {free_cpu_cores:.2f} Cores Free
CPU Utilization     : {cpu_usage_pct:.2f}%

RAM Capacity        : {total_ram_gib:.2f} GiB Total | {used_ram_gib:.2f} GiB Used | {free_ram_gib:.2f} GiB Free
RAM Utilization     : {ram_usage_pct:.2f}%

--- POD CAPACITY SCHEDULING ---
Pod Requirement     : {pod_ram_gib:.2f} GiB RAM
Max Deployable      : {max_pods} Pods
Remaining Headroom  : {remaining_headroom_gib:.2f} GiB RAM
======================================================================"""

print(report)
