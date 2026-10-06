import re

# ==============================================================================
# HOMEWORK: Gateway Telemetry Incident Triage
# ==============================================================================
# Background:
# A production API gateway experienced an influx of suspicious requests and
# server errors. The operations team collected a batch of raw log strings from
# the gateway. Your goal is to parse, filter, sanitize, and extract incident
# metrics using Regular Expressions (`re`), `lambda`, `map()`, and `filter()`.
#
# Constraints:
# - Do not use traditional 'for' loops for transformations or filtering.
# - Use 'map()' and 'filter()' with 'lambda' functions as specified in each task.
# - Do not import external libraries; use Python standard library ('re').
# ==============================================================================

# --- Raw Telemetry Fixtures (Do not modify this list) ---
RAW_LOGS = [
    "2026-10-06 14:01:05 [ALERT] client=192.168.1.105 method=GET path=/api/v1/health status=200 latency=15ms",
    "2026-10-06 14:01:09 [ALERT] client=10.0.0.19 method=POST path=/api/v1/auth status=401 latency=88ms",
    "2026-10-06 14:01:14 [ALERT] client=198.51.100.44 method=GET path=/admin/config status=403 latency=12ms",
    "2026-10-06 14:01:22 [ALERT] client=203.0.113.89 method=POST path=/api/v1/checkout status=500 latency=1420ms",
    "2026-10-06 14:01:30 [ALERT] client=10.0.0.42 method=GET path=/metrics status=200 latency=24ms",
    "2026-10-06 14:01:37 [ALERT] client=198.51.100.44 method=POST path=/admin/dump status=403 latency=9ms",
    "2026-10-06 14:01:45 [ALERT] client=203.0.113.89 method=GET path=/api/v1/reports status=504 latency=3100ms",
    "2026-10-06 14:01:52 [ALERT] client=192.168.1.200 method=GET path=/static/app.js status=304 latency=5ms",
    "2026-10-06 14:02:01 [ALERT] client=10.0.0.19 method=POST path=/api/v1/auth status=401 latency=95ms",
    "2026-10-06 14:02:10 [ALERT] client=203.0.113.99 method=POST path=/api/v1/payment status=502 latency=2850ms",
]
# --------------------------------------------------------


# ------------------------------------------------------------------------------
# TASK 1: Regular Expression Patterns
# ------------------------------------------------------------------------------
# Define regex patterns as raw strings (r"...") to match the following fields:
# - IP_PATTERN: Matches an IPv4 address (e.g., 192.168.1.105)
# - STATUS_PATTERN: Matches 3-digit status codes after 'status=' (e.g., 401, 500)
# - LATENCY_PATTERN: Matches integer digits before 'ms' after 'latency=' (e.g., 1420)

# TODO 1: Define the regex patterns
IP_PATTERN = r""
STATUS_PATTERN = r""
LATENCY_PATTERN = r""


# ------------------------------------------------------------------------------
# TASK 2: Filter Error Logs (4xx and 5xx)
# ------------------------------------------------------------------------------
# Use 'filter()' and a 'lambda' function to extract all log lines from RAW_LOGS
# where the HTTP status code is an error (status >= 400).
# Hint: You can use re.search() inside the lambda to match status codes starting
# with 4 or 5 (e.g., r"status=[45]\d{2}"), or parse the status integer.

# TODO 2: Filter error logs into a list
# error_logs = list(filter(...))
error_logs = []

print(f"Task 2 - Error Logs Found: {len(error_logs)}")


# ------------------------------------------------------------------------------
# TASK 3: Filter High-Latency Slow Requests (>= 1000ms)
# ------------------------------------------------------------------------------
# Performance SLA is breached when a request takes 1000ms or longer.
# Use 'filter()' and a 'lambda' function to extract all lines from RAW_LOGS
# where the numeric latency is >= 1000.
# Hint: Use re.search(r"latency=(\d+)ms", log) and convert group(1) to int.

# TODO 3: Filter slow requests into a list
# slow_requests = list(filter(...))
slow_requests = []

print(f"Task 3 - Slow Requests Found: {len(slow_requests)}")


# ------------------------------------------------------------------------------
# TASK 4: Sanitize IP Addresses with map() and re.sub()
# ------------------------------------------------------------------------------
# Before exporting logs to an external analytics vendor, sanitize all IP
# addresses by replacing them with "[REDACTED_IP]".
# Use 'map()' and a 'lambda' function that calls re.sub(IP_PATTERN, "[REDACTED_IP]", line)
# on each line of RAW_LOGS.

# TODO 4: Transform RAW_LOGS into sanitized logs
# sanitized_logs = list(map(...))
sanitized_logs = []

print(f"Task 4 - Sanitized Logs Sample: {sanitized_logs[:1] if sanitized_logs else []}")


# ------------------------------------------------------------------------------
# TASK 5: Extract Structured Incident Summaries with map()
# ------------------------------------------------------------------------------
# Take the 'error_logs' list from Task 2.
# Use 'map()' and a 'lambda' function to convert each error log string into a
# clean incident summary string formatted exactly as:
#   "[INCIDENT] Client: <ip> | Path: <path> | Status: <status>"
# Example:
#   "[INCIDENT] Client: 10.0.0.19 | Path: /api/v1/auth | Status: 401"
# Hint: Use re.search() with capture groups or separate search calls inside the lambda.

# TODO 5: Map error_logs into incident summary strings
# incident_summaries = list(map(...))
incident_summaries = []

print(f"Task 5 - Incident Summaries Generated: {len(incident_summaries)}")


# ------------------------------------------------------------------------------
# TASK 6: Pipeline Composition (Chaining filter() and map())
# ------------------------------------------------------------------------------
# Build a functional processing pipeline in a single expression that:
# 1. Filters RAW_LOGS to keep ONLY 5xx server errors (status 500, 502, 504).
# 2. Maps the filtered lines to extract ONLY the client IP address string.
# 3. Wraps the result into a list (or set to remove duplicates).

# TODO 6: Chain filter() and map() to extract client IPs causing 5xx errors
# server_fault_ips = list(map(..., filter(..., RAW_LOGS)))
server_fault_ips = []

print(f"Task 6 - Unique Client IPs on 5xx Errors: {set(server_fault_ips)}")
