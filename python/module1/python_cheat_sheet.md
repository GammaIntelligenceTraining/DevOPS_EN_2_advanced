# Module 1: Python Fundamentals for DevOps — Cheat Sheet

## 1. Primitive Data Types Matrix

Python dynamically assigns types at runtime. Use this reference to verify type characteristics, valid literal syntax, and standard systems engineering use cases.

| Type | Name | Literal Examples | DevOps Sysadmin Context |
| :--- | :--- | :--- | :--- |
| `int` | Integer | `22`, `8080`, `1048576`, `-1` | TCP/UDP ports, PIDs, HTTP status codes, byte counters |
| `float` | Floating-point | `0.75`, `99.99`, `1.45`, `0.0` | Load averages, disk utilization percentages, SLA uptime ratios |
| `str` | String | `"web01"`, `'10.0.0.1'`, `"active"` | Hostnames, IP addresses, log lines, systemd unit names |
| `bool` | Boolean | `True`, `False` | Daemon running states, maintenance flags, automated health status |

---

## 2. Explicit Type Conversion (Casting) & Falsy Values

Input received from terminal prompts (`input()`), environment variables, or log files is always of type `str`. Use explicit conversion functions to transform data types safely.

| Function | Target Type | Input Example | Output Value | DevOps Use Case / Behavior |
| :--- | :--- | :--- | :--- | :--- |
| `int(x)` | `int` | `int("8080")` | `8080` | Converts numeric string to whole integer. Raises `ValueError` if decimal or text. |
| `float(x)` | `float` | `float("1.85")` | `1.85` | Parses decimal strings into IEEE 754 floating-point numbers. |
| `str(x)` | `str` | `str(443)` | `"443"` | Serializes numeric values or booleans to string format for logging/display. |
| `bool(x)` | `bool` | `bool("1")` | `True` | Converts value to boolean based on truthiness rules. |

### Truthiness & Falsy Evaluation Rules

In boolean contexts, Python evaluates the following values as `False` (falsy):
- Constants: `None`, `False`
- Numeric zeros: `0`, `0.0`
- Empty collections/strings: `""`, `[]`, `{}`, `()`, `set()`

All other values evaluate to `True` (truthy).

> [!WARNING]
> Any non-empty string evaluates to `True`! For example, `bool("0")` and `bool("False")` both evaluate to `True` because their string length is greater than zero.

### Safe Operator Input Pattern with Default Fallback

The boolean `or` operator allows setting default fallback values when an operator presses Enter without providing an input:

```python
raw_input = input("Enter port [default 8080]: ").strip()
port = int(raw_input or "8080")
```

---

## 3. Special String Characters, Escapes & Raw Strings

Special characters in Python strings are escaped using a backslash (`\`).

| Sequence | Name | Rendered Behavior | DevOps Sysadmin Context |
| :---: | :--- | :--- | :--- |
| `\n` | Newline | Inserts a line break | Formatting multiline console reports, reading line-delimited log files |
| `\t` | Tab | Inserts a horizontal tab | Parsing tab-separated telemetry (TSV), indenting CLI output columns |
| `\\` | Backslash | Inserts a literal backslash | Specifying Windows filesystem paths (`C:\\Windows\\System32`) |
| `\'` | Single Quote | Inserts literal `'` inside `'...'` | Nesting quotes inside shell commands (`'echo \'hello\''`) |
| `\"` | Double Quote | Inserts literal `"` inside `"..."` | Constructing JSON strings or wrapping CLI arguments with double quotes |
| `r"..."` | Raw String | Suppresses escape processing | Writing regular expression patterns (`r"^10\.\d{1,3}"`) |
| `"""..."""`| Triple Quote | Preserves multiline blocks | Embedding raw configuration file templates (Nginx, systemd unit files) |

---

## 4. String Indexing, Slicing & Membership Reference

Strings are zero-indexed sequences of characters. Slicing extracts substrings without modifying the original string.

```text
 Index:   0   1   2   3   4   5   6   7   8   9  10  11  12  13  14  15
 Char :   s   r   v   -   u   s   -   e   a   s   t   -   w   e   b   1
-Index: -16 -15 -14 -13 -12 -11 -10  -9  -8  -7  -6  -5  -4  -3  -2  -1
```

| Operation | Syntax | Example (`s = "srv-us-east-web1"`) | Result | DevOps Infrastructure Use Case |
| :--- | :--- | :--- | :--- | :--- |
| First character | `s[0]` | `s[0]` | `'s'` | Inspecting initial character or protocol flag |
| Last character | `s[-1]` | `s[-1]` | `'1'` | Extracting trailing node index or drive letter |
| Substring slice | `s[start:stop]` | `s[0:3]` | `'srv'` | Extracting server role or tier prefix |
| Prefix slice | `s[:stop]` | `s[:7]` | `'srv-us-'` | Extracting region and environment prefix |
| Suffix slice | `s[start:]` | `s[12:]` | `'web1'` | Extracting instance name or trailing role |
| Negative slice | `s[-4:]` | `s[-4:]` | `'web1'` | Extracting fixed-width tail identifier |
| Strided slice | `s[::step]` | `s[::2]` | `'svu-atwb'` | Skipping characters in fixed-width records |
| Reverse string | `s[::-1]` | `s[::-1]` | `'1bew-tsae-su-vrs'` | Inverting strings for suffix-based sorting |
| Out-of-bounds slice | `s[12:999]` | `s[12:999]` | `'web1'` | **Safe:** Slicing never raises `IndexError` (unlike direct indexing `s[999]`) |
| String membership | `sub in s` | `'east' in s` | `True` | Fast substring detection in hostnames or log lines |
| Negative membership | `sub not in s` | `'prd' not in s` | `True` | Confirming absence of specific flags or keywords |

---

## 5. DevOps String Methods Reference Matrix

Strings in Python are immutable objects. String methods return a newly modified string without altering the original variable.

| Method | Syntax | Input Example | Output | DevOps Automation Use Case |
| :--- | :--- | :--- | :--- | :--- |
| `.strip()` | `s.strip()` | `"  /var/log  \n"` | `"/var/log"` | Stripping trailing newlines and whitespace from log lines or file reads |
| `.lstrip()` | `s.lstrip()` | `"--verbose"` | `"verbose"` | Removing leading CLI prefixes or comment hashes (`#`) |
| `.rstrip()` | `s.rstrip()` | `"nginx.conf\n"` | `"nginx.conf"` | Stripping trailing line breaks while preserving leading indentation |
| `.lower()` | `s.lower()` | `"GET"` | `"get"` | Normalizing HTTP request verbs and DNS domain names |
| `.upper()` | `s.upper()` | `"warning"` | `"WARNING"` | Standardizing severity tokens for alerting engines |
| `.startswith()` | `s.startswith(sub)` | `"[ERROR] 502"` | `True` | Rapid log filtering and triage of syslog/journal lines |
| `.endswith()` | `s.endswith(sub)` | `"backup.tar.gz"` | `True` | Auditing file extensions during filesystem sweeps |
| `.replace()` | `s.replace(old, new)`| `"http://api"` | `"https://api"` | Sanitizing URLs, normalizing paths, or masking secrets |
| `.split()` | `s.split(sep)` | `"10.0.0.1:80"` | `['10.0.0.1', '80']` | Splitting delimited endpoints and CSV telemetry rows (teaser for M2) |
| `.count()` | `s.count(sub)` | `"404 500 404"` | `2` | Counting specific error code occurrences in log buffers |
| `len()` | `len(s)` | `len("password123")`| `11` | Verifying token lengths and packet payload sizes |

---

## 6. Arithmetic & Capacity Math Operators

Arithmetic operators calculate storage limits, worker allocations, and throughput. Python evaluates operators according to standard mathematical precedence.

| Operator | Name | Syntax | Result | Precedence | DevOps Capacity Use Case |
| :---: | :--- | :--- | :---: | :---: | :--- |
| `**` | Exponentiation | `1024 ** 3` | `1073741824` | 1 (Highest) | Computing IEC binary unit multipliers ($1024^3$ = 1 GiB) |
| `*` | Multiplication | `4 * 1024` | `4096` | 2 | Converting Gibibytes to Mebibytes |
| `/` | True Division | `15 / 2` | `7.5` | 2 | Calculating resource usage percentages (always returns float) |
| `//` | Floor Division | `15 // 2` | `7` | 2 | Calculating maximum deployable worker pods that fit in RAM |
| `%` | Modulo | `15 % 2` | `1` | 2 | Computing unallocated RAM remainder after pod deployment |
| `+` | Addition | `1024 + 512` | `1536` | 3 | Summing resource limits across multi-container specs |
| `-` | Subtraction | `32.0 - 24.0`| `8.0` | 3 (Lowest) | Calculating available free memory or disk headroom |

### Augmented Assignment Operators

Augmented assignment operators mutate a variable in-place by performing an operation and reassigning the result:

| Operator | Equivalent Syntax | Example | Description |
| :---: | :--- | :--- | :--- |
| `+=` | `x = x + y` | `retry_count += 1` | Increment event counters or retry counters |
| `-=` | `x = x - y` | `remaining_ram -= pod_ram` | Deduct consumed allocations from available resource pools |
| `*=` | `x = x * y` | `backoff_ms *= 2` | Exponential backoff multipliers |
| `/=` | `x = x / y` | `rate /= 1000` | Scale units (e.g. milliseconds to seconds) |
| `//=`| `x = x // y`| `capacity //= 2` | Halve maximum worker allocations |

---

## 7. Modern f-String Formatting Reference

Formatted string literals (f-strings) provide readable and performant string interpolation. Expressions inside curly braces `{}` are evaluated at runtime.

| Format Specifier | Purpose | Input Value | Syntax Example | Rendered Output |
| :--- | :--- | :--- | :--- | :--- |
| `:.2f` | Round to 2 decimal places | `74.8912` | `f"{74.8912:.2f}%"` | `74.89%` |
| `:.0f` | Round to nearest integer | `99.8` | `f"{99.8:.0f}%"` | `100%` |
| `:<18` | Left-align in 18 characters | `"node-01"` | `f"{'node-01':<18}"` | `'node-01          '` |
| `:>10` | Right-align in 10 characters | `42` | `f"{42:>10}"` | `'        42'` |
| `:04d` | Pad integer with leading zeros | `7` | `f"{7:04d}"` | `'0007'` |
| `:,` | Group thousands with commas | `17179869184` | `f"{17179869184:,}"` | `'17,179,869,184'` |

### Multi-Column Table Output Pattern

```python
print(f"{'SERVER':<18} {'IP':<16} {'RAM (GiB)':>10}")
print("-" * 46)
print(f"{'web-01':<18} {'10.0.1.10':<16} {32.0:>10.2f}")
```

---

## 8. VS Code & Dual-Platform Execution Reference

In this module, scripts are authored and executed natively on your host workstation inside **Visual Studio Code**.

### Windows Workstation (PowerShell inside VS Code)

Initialize and activate an isolated virtual environment in your workspace root:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

If PowerShell displays a script execution policy error (`PSSecurityException`), run the following command once to permit local scripts:

```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

Execute your script using the active virtual environment interpreter:

```powershell
python script.py
```

### macOS Workstation (Terminal inside VS Code)

Initialize and activate an isolated virtual environment in your workspace root:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Execute your script using the active virtual environment interpreter:

```bash
python3 script.py
```

### Essential VS Code Shortcuts

| Action | Windows Shortcut | macOS Shortcut | Command Palette / Navigation |
| :--- | :--- | :--- | :--- |
| Open Command Palette | `Ctrl + Shift + P` | `Cmd + Shift + P` | Search commands and extensions |
| Select Python Interpreter | `Ctrl + Shift + P` | `Cmd + Shift + P` | Type `Python: Select Interpreter` $\to$ pick `.venv` |
| Toggle Integrated Terminal | `Ctrl + \`` | `Cmd + \`` | View $\to$ Terminal |
| Run Python File | Play Icon | Play Icon | Click triangular Run button in top-right editor tab |
| Clear Terminal | `Ctrl + L` or `cls` | `Ctrl + L` or `clear`| Resets terminal scrollback buffer |
