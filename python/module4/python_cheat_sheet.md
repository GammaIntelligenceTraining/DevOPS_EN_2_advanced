# Python for DevOps: Module 4 Cheat Sheet
**Focus:** File I/O, Exceptions, and JSON Serialization.

## 1. Exception Handling
Exceptions act as defensive guardrails. If a block of code crashes, an exception is thrown. If uncaught, the script terminates.

| Statement | Syntax Example | Description |
| :--- | :--- | :--- |
| **try** | `try:` | Wraps risky code that might crash. |
| **except** | `except ValueError:` | Catches a specific error type to prevent a crash. |
| **except (catch-all)**| `except Exception as e:`| Catches ANY error and saves the error message to `e`. |
| **else** | `else:` | Runs **only** if the `try` block succeeded. |
| **finally** | `finally:` | Runs **always**, regardless of success or failure. |
| **raise** | `raise RuntimeError("Crash")` | Manually triggers an error. |

### Common Built-In Exceptions
| Exception Type | Common Cause |
| :--- | :--- |
| `ValueError` | Converting invalid data types (e.g., `int("abc")`). |
| `KeyError` | Looking up a dictionary key that doesn't exist (e.g., `my_dict["missing"]`). |
| `IndexError` | Accessing a list index that is out of bounds (e.g., `my_list[99]`). |
| `FileNotFoundError` | Trying to read a file path that doesn't exist. |

---

## 2. File I/O (Input / Output)
Always use the `with` context manager when opening files. It guarantees the file descriptor is closed securely, preventing OS resource leaks.

### I/O Modes
| Mode | String | Description |
| :--- | :--- | :--- |
| **Read** | `"r"` | Default mode. Opens file for reading. Crashes if file is missing. |
| **Write** | `"w"` | Opens file for writing. **OVERWRITES** entire file. Creates if missing. |
| **Append** | `"a"` | Opens file for appending. Adds to the end. Creates if missing. |
| **Exclusive**| `"x"` | Opens for exclusive creation. **Crashes** if file already exists. |
| **Read/Write**| `"r+"`| Opens for both reading and writing without truncating first. |
| **Binary** | `"rb"` | Opens in binary mode (reads raw bytes, not text). |

### File Methods
| Method | Example | Description |
| :--- | :--- | :--- |
| **Open safely** | `with open("log.txt", "r") as f:`| Opens file, assigns it to variable `f`, and auto-closes it later. |
| **Read all** | `content = f.read()` | Reads the entire file into a single string (dangerous for large logs). |
| **Read line** | `line = f.readline()` | Reads exactly one line from the file. |
| **Read all lines**| `lines = f.readlines()`| Reads the entire file into a List of strings. |
| **Iterate lines** | `for line in f:` | Streams one line at a time (highly memory efficient). |
| **Strip newlines**| `line = line.strip()` | Removes trailing `\n` characters from string edges. |
| **Write data** | `f.write("Hello\n")` | Writes a string to the file. You must explicitly include `\n`. |
| **Close** | `f.close()` | Manually closes the file (not needed if using `with`). |
| **Check closed** | `f.closed` | Property that returns `True` if the file is closed. |

---

## 3. Structured Data (JSON)
JSON is a text format that is functionally identical to Python dictionaries and lists.

| Method | Example | Description |
| :--- | :--- | :--- |
| **`json.loads()`** | `dict_obj = json.loads(json_str)`| Converts a JSON **string** into a Python Dictionary. |
| **`json.dumps()`** | `json_str = json.dumps(dict_obj)`| Converts a Python Dictionary into a JSON **string**. |
| **`json.dump()`** | `json.dump(dict_obj, f)` | Writes a Python Dictionary directly into an open file. |
| **`json.load()`** | `dict_obj = json.load(f)` | Reads directly from an open file into a Python Dictionary. |

*Note: Use the `indent=4` argument in `dumps()` or `dump()` to make the JSON human-readable (pretty-printed).*

---

## 4. Functional Tools (map, filter, zip)
When working with hundreds of servers or parsing logs, transforming and combining lists is extremely common. These functions all return memory-efficient generator objects, so we wrap them in `list()` to see the results immediately.

| Method | Example | Description |
| :--- | :--- | :--- |
| **`map()`** | `list(map(int, ["80", "443"]))` | Applies a function (like `int`) to every single item in the iterable. |
| **`filter()`**| `list(filter(is_ok, statuses))` | Keeps only the items where the provided function returns `True`. |
| **`zip()`** | `list(zip(hosts, ips))` | Pairs items index-by-index `(hosts[0], ips[0])` like a jacket zipper. |
| **`dict(zip())`**| `dict(zip(hosts, ips))` | Instantly creates a Dictionary using the first list as Keys and the second as Values. |
