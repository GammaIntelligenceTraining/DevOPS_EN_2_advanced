# Module 2: Collections & Control Flow — Cheat Sheet

## 1. Comparison & Identity Operators Matrix

Comparison operators evaluate expressions and return a boolean (`True` or `False`). In systems automation, they drive threshold triggers, service state validation, and capacity gates.

| Operator | Meaning | Syntax Example | Evaluation & Behavioral Rule |
| :--- | :--- | :--- | :--- |
| `==` | Value equality | `status == "online"` | Evaluates to `True` if values or contents match identically. |
| `!=` | Value inequality | `http_code != 200` | Evaluates to `True` if values differ. |
| `<` | Strictly less than | `disk_free_gb < 15` | Evaluates to `True` if left operand is strictly smaller than right. |
| `>` | Strictly greater than | `cpu_load > 85.0` | Evaluates to `True` if left operand is strictly larger than right. |
| `<=` | Less than or equal | `active_pods <= max_pods` | Evaluates to `True` if left operand is smaller than or equal to right. |
| `>=` | Greater than or equal | `retries >= 3` | Evaluates to `True` if left operand is greater than or equal to right. |
| `is` | Object identity | `leader is None` | Evaluates to `True` if both operands point to the exact same memory address. |
| `is not` | Negated identity | `gateway is not None` | Evaluates to `True` if operands refer to distinct objects in memory. |

### Chained Comparisons (Pythonic Range Checking)

Python allows chaining comparison operators together into natural mathematical expressions. The expression `a < b < c` is equivalent to `(a < b) and (b < c)`, but evaluates `b` only once.

The following snippet demonstrates range checking for ports and metrics using Pythonic chained comparisons:

```python
# Verify if port number is within the valid unprivileged range (1024 to 65535)
is_valid_port = 1024 <= port <= 65535

# Verify if CPU percentage is within normal baseline thresholds
is_nominal = 10.0 <= cpu_utilization < 75.0
```

### Comparison Variations, Quirks & Common Pitfalls

| Scenario / Variation | Code Example | Result | Explanation & Best Practice |
| :--- | :--- | :--- | :--- |
| Numeric equivalence | `42 == 42.0` | `True` | Python evaluates mathematical equivalence across `int` and `float`. |
| Cross-type equality | `42 == "42"` | `False` | Python never implicitly coerces strings to numbers during comparison. |
| Cross-type ordering | `42 < "42"` | `TypeError` | Python 3 disallows relative ordering (`<`, `>`) between mismatched types. |
| String number trap | `"10" < "2"` | `True` | Strings compare character-by-character by ASCII code (`"1"` < `"2"`). Always cast to `int`! |
| String case-sensitivity | `"admin" == "Admin"` | `False` | String comparisons are strictly case-sensitive. Use `.lower()` before comparing. |
| Float precision pitfall | `0.1 + 0.2 == 0.3` | `False` | Binary floating-point representation causes tiny rounding errors (`0.30000000000000004`). |
| Safe float comparison | `round(0.1 + 0.2, 4) == 0.3` | `True` | Round floating-point calculations or check `abs(a - b) < 1e-9` before equality checks. |

### PEP 8 Comparison Best Practices

The following patterns represent Python standard engineering conventions:

| Recommended Pattern (DO) | Discouraged Pattern (DON'T) | Rationale |
| :--- | :--- | :--- |
| `if leader is None:` | `if leader == None:` | `None` is a memory singleton; `is` tests pointer identity directly and fast. |
| `if gateway is not None:` | `if not gateway is None:` | `is not` is the idiomatic, readable Python operator. |
| `if is_healthy:` | `if is_healthy == True:` | Explicit `== True` is redundant and unpythonic. |
| `if not is_healthy:` | `if is_healthy == False:` | Explicit `== False` is redundant; use `not` instead. |

> [!WARNING]
> Always use `==` for comparing values (strings, numbers, lists). Use `is` strictly for comparing against `None` or boolean singletons (`True`/`False`). Comparing strings or numbers with `is` can lead to unpredictable behavior across CPython optimizations.

---

## 2. Logical Operators & Short-Circuit Evaluation

Logical operators combine multiple boolean expressions to form composite control gates.

| Operator | Syntax Pattern | Rule / Behavior | DevOps Example |
| :--- | :--- | :--- | :--- |
| `and` | `cond1 and cond2` | Evaluates to `True` only if **both** operands are `True`. | `is_online and (cpu_pct < 80)` |
| `or` | `cond1 or cond2` | Evaluates to `True` if **at least one** operand is `True`. | `disk_pct >= 90 or mem_pct >= 90` |
| `not` | `not cond` | Reverses boolean state (`True` -> `False`, `False` -> `True`). | `not is_maintenance_mode` |

### Short-Circuit Evaluation Mechanics

Python evaluates logical expressions from left to right and stops as soon as the final outcome is determined:
- In `A and B`: If `A` is `False`, Python never evaluates `B` because the expression can never be `True`.
- In `A or B`: If `A` is `True`, Python never evaluates `B` because the expression is already `True`.

Before verifying nested telemetry attributes, use short-circuiting to prevent runtime crashes when objects or metrics are absent:

```python
# The second check will never execute if server_record is None or empty
has_healthy_cpu = (server_record is not None) and (server_record.get("cpu", 100) < 80)
```

---

## 3. Conditional Branching (`if`, `elif`, `else`) & Decision Patterns

Python uses 4-space indentation to define conditional code blocks. Conditions are evaluated sequentially from top to bottom.

### Standalone `if` Statements (Without `else` or `elif`)

An `else` branch is optional. Use a standalone `if` when an action should only execute if a condition is met, without performing any alternative action when False:

The following example conditionally updates an access control flag without requiring an alternative branch:

```python
# Standalone guard: only elevates permissions if role matches
elevated_access = False
if user_role == "admin":
    elevated_access = True
```

### Truthiness Without Direct Comparison (`if name:`, `if not name:`)

In Python, every object has an inherent boolean truth value. You do not need to write `if name != "":` or `if count > 0:`. Testing the object directly evaluates its truthiness:

The following code demonstrates inspecting presence of values without verbose comparison operators:

```python
# Falsy: "", 0, 0.0, None, False, [], {}, ()
# Truthy: non-empty strings, non-zero numbers, populated collections

if username:
    print(f"Logged in as {username}")

if not api_token:
    print("Warning: Missing API token, fallback to anonymous tier")
```

### Nested `if` Statements (Hierarchical Decisions)

An `if` statement can reside inside another `if` block. While `if A and B:` evaluates multiple conditions simultaneously, nested `if` blocks allow executing distinct code or providing specific diagnostic messages at each stage of a multi-step evaluation:

The following example illustrates a hierarchical validation flow for verifying user authentication before inspecting role permissions:

```python
if is_authenticated:
    print("Identity confirmed.")
    if user_role == "admin":
        print("Admin access granted.")
    else:
        print("Standard read-only access granted.")
else:
    print("Authentication failed.")
```

### Tiered Health Triage (`if`, `elif`, `else`)

When multiple mutually exclusive conditions must be evaluated in order, use `elif` branches followed by a catch-all `else` block:

The following script categorizes host severity by inspecting packet loss and round-trip latency against operational thresholds:

```python
packet_loss_pct = 3.5
latency_ms = 180

if packet_loss_pct >= 5.0 or latency_ms >= 500:
    severity = "CRITICAL"
elif packet_loss_pct >= 2.0 or latency_ms >= 200:
    severity = "WARNING"
else:
    severity = "OK"
```

### Membership Testing (`in` / `not in`)

The `in` keyword verifies whether an element exists inside a collection (string, list, set, or dictionary keys).

The following example inspects whether a server hostname contains a specific production prefix:

```python
hostname = "web-prod-us-east-01"

if "prod" in hostname:
    is_production = True
```

---

## 4. Lists Quick Reference

A list is an ordered, zero-indexed, mutable sequence enclosed in brackets `[]`.

### Lists Operations & Methods Matrix

| Operation | Syntax | Description | Example / Context |
| :--- | :--- | :--- | :--- |
| Create empty | `nodes = []` | Initializes an empty list | Dynamically accumulating hosts |
| Homogeneous list | `["web01", "web02"]` | List containing elements of the same type | Standard server inventory |
| Heterogeneous list | `["db01", 5432, True]` | List containing mixed data types | Multi-field telemetry record |
| Indexing | `nodes[0]`, `nodes[-1]` | Accesses element by zero-based or negative index | Inspecting first or last node |
| In-place update | `nodes[0] = "primary"` | Modifies element at specific index ($O(1)$) | Updating designated cluster leader |
| Slicing | `nodes[0:2]` | Returns sub-list from index 0 to 1 | Isolating primary availability zone |
| Length | `len(nodes)` | Returns total item count | Verifying autoscaling limits |
| Append | `nodes.append("web03")` | Appends a **single** element to the end ($O(1)$) | Adding individual node to pool |
| Insert | `nodes.insert(1, "canary")` | Inserts single element at specified index ($O(n)$) | Pinning canary node at index 1 |
| Unpack to variables | `host, port = ["web01", 80]` | Unpacks elements into individual variables | Extracting structured telemetry fields |
| Unpack (`*list`) | `[*east, *west]` | Unpacks elements into a new list or function call | Merging fleets without mutating originals |
| Pop | `nodes.pop()` | Removes and returns element at index (default last) | Decommissioning newest worker node |
| Remove | `nodes.remove("web02")` | Removes first matching value; raises `ValueError` if absent | Draining and deleting specific host |
| Safe Remove | `if host in nodes: nodes.remove(host)` | Guards against `ValueError` before removing | Safe automated node decommissioning |
| Clone (`.copy()`) | `backup = nodes.copy()` | Creates an independent shallow copy | Preventing pointer aliasing bugs |
| Membership | `"web01" in nodes` | Checks if element is present in collection | Validating authorized gateway hosts |
| Numeric sum | `sum(cpu_metrics)` | Calculates total sum of numeric elements | Aggregating cluster utilization |
| Min / Max | `min(loads)`, `max(loads)` | Finds lowest or highest numeric value | Identifying cluster bottleneck |

### Sequence Unpacking to Variables (Multiple Assignment)

List elements can be unpacked directly into individual variables on a single line. The variable count on the left must match the number of items in the list:

The following snippet unpacks a server telemetry row into discrete endpoint identifiers:

```python
# Unpack fixed-length list directly into individual variables
endpoint = ["10.0.1.50", 443, "online"]
ip_address, port_number, service_status = endpoint

# Unpack first element and gather remaining elements with *rest
primary_node, *replica_nodes = ["db-01", "db-02", "db-03"]
```

### Pointer Aliasing vs. Independent Copying (`.copy()`)

In Python, variables store memory references (pointers) to objects. The assignment operator `b = a` does **not** create a new list; it merely creates a second pointer to the exact same list in memory. Mutating `b` will unintentionally mutate `a`.

To create an independent copy that can be modified safely without affecting the original, always use `.copy()` or list slicing `[:]`:

```python
# PITFALL: Pointer Aliasing (b = a)
fleet_a = ["web01", "web02"]
fleet_b = fleet_a
fleet_b.append("web03")
# Result: fleet_a is now ['web01', 'web02', 'web03']!

# BEST PRACTICE: Independent Shallow Copy (.copy())
base_fleet = ["web01", "web02"]
active_fleet = base_fleet.copy()
active_fleet.append("web03")
# Result: active_fleet has 3 items, base_fleet remains safely at 2 items
```

### Append vs. Extend vs. Unpack (`*list`)

Understanding the distinction between `.append()`, `.extend()`, and `*list` is critical when combining collections:

The following code illustrates how passing a list to `.append()` creates an unwanted nested list, whereas `.extend()` and `*list` flatten elements:

```python
cluster = ["node01", "node02"]

# WRONG: .append() nests the list as a single child element
# cluster.append(["node03", "node04"]) -> ["node01", "node02", ["node03", "node04"]]

# CORRECT: .extend() mutates the list in-place by adding each element
cluster.extend(["node03", "node04"])

# CORRECT: *list unpacking combines lists into a brand new list
merged = [*cluster, "node05"]
```

---

## 5. Loops & Iteration Control Matrix

Loops automate repetitive inspection across fleet inventories, log streams, and retry queues.

### Loops Operations & Control Matrix

| Construct | Syntax Pattern | Description | Primary DevOps Use Case |
| :--- | :--- | :--- | :--- |
| `for ... in list` | `for host in hosts:` | Iterates over each item in a sequence | Processing server inventory lists |
| `range(stop)` | `for i in range(3):` | Generates integers from `0` to `stop - 1` | Zero-indexed repeat iterations |
| `range(start, stop)` | `for attempt in range(1, 4):` | Generates integers from `start` to `stop - 1` | Formatted retry attempt counters |
| `range(start, stop, step)` | `for port in range(8080, 8086, 2):` | Increments by custom step size | Stepped port allocation loops |
| Countdown range | `for sec in range(5, 0, -1):` | Decrements using negative step value | Maintenance reboot countdown timers |
| Guarded `while True` | `while True: ... if ready: break` | Infinite loop terminated by internal condition | Background daemon worker queues |
| Safe loop mutation | `for x in my_list.copy():` | Iterates over independent shallow copy | Safe list pruning without index shift |

### Numerical Sequences with `range()`

The `range()` function generates arithmetic sequences on demand without allocating entire lists in memory. It accepts one, two, or three arguments: `range(stop)`, `range(start, stop)`, and `range(start, stop, step)`:

The following snippet demonstrates standard retry counters, stepped port traversal, and a reverse maintenance countdown:

```python
# Retry attempts: range(1, 4) produces 1, 2, 3
for attempt in range(1, 4):
    print(f"Deploy attempt {attempt} of 3")

# Stepping by 2: range(8080, 8086, 2) produces 8080, 8082, 8084
for port in range(8080, 8086, 2):
    print(f"Checking listener port: {port}")

# Reverse countdown: range(3, 0, -1) produces 3, 2, 1
for seconds in range(3, 0, -1):
    print(f"Restarting service in {seconds}s...")
```

### The Mutation-During-Iteration Anti-Pattern

Modifying the length of a list while iterating directly over it (`for item in my_list: my_list.remove(item)`) causes Python's internal index pointer to shift, silently skipping elements:

The following snippet demonstrates the element skipping bug and its production resolution:

```python
# THE BUG: Modifying list during loop skips elements
nodes = ["web-01", "web-02", "web-03", "web-04"]
for host in nodes:
    if "02" in host or "03" in host:
        nodes.remove(host)
# Result: 'web-03' was silently skipped because index shifted left!

# THE FIX: Iterate over an independent copy (.copy())
clean_nodes = ["web-01", "web-02", "web-03", "web-04"]
for host in clean_nodes.copy():
    if "02" in host or "03" in host:
        clean_nodes.remove(host)
# Result: Both 'web-02' and 'web-03' are removed correctly
```

---

## 6. Dual-Platform VS Code Execution Reference

Follow these platform-specific commands in the VS Code integrated terminal to execute scripts within your isolated virtual environment (`.venv`).

### Windows (PowerShell)

Verify that the active terminal shows `(.venv)` in the command prompt before executing scripts:

```powershell
# Activate local workspace virtual environment
.\.venv\Scripts\Activate.ps1

# Execute Python script
python handout.py
```

### macOS / Linux (Terminal)

Verify that the active terminal shows `(.venv)` in the shell prompt before executing scripts:

```bash
# Activate local workspace virtual environment
source .venv/bin/activate

# Execute Python script
python3 handout.py
```
