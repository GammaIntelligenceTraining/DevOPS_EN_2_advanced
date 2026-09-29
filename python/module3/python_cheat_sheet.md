# Python Module 3 Cheat Sheet: Advanced Collections & Functions

## 1. Dictionaries Quick Reference
Dictionaries map `keys` to `values`. Keys must be immutable (strings, integers, tuples).

| Operation / Method | Syntax Example | Description |
| :--- | :--- | :--- |
| **Creation** | `node = {"ip": "10.0.0.1", "cpu": 85}` | Creates a new dictionary. |
| **Read (Direct)** | `val = node["cpu"]` | Returns value. **Fatal `KeyError` if key missing.** |
| **Read (Safe)** | `val = node.get("cpu", 0)` | Returns value, or default `0` if key is missing. |
| **Mutate / Add** | `node["ram"] = 64` | Adds a new key-value pair, or updates existing key. |
| **Remove Key** | `val = node.pop("cpu")` | Removes the key and returns its value. |
| **Keys List** | `node.keys()` | Returns a view of all keys. |
| **Values List** | `node.values()` | Returns a view of all values. |
| **Items List** | `node.items()` | Returns a view of `(key, value)` tuples for iteration. |

```python
# Iterating over a dictionary
for key, value in node.items():
    print(f"{key}: {value}")
```

## 2. Tuples & Sets Matrix
### Tuples
Tuples are **immutable** lists. They cannot be appended, popped, or changed after creation.

| Concept | Syntax Example | Description |
| :--- | :--- | :--- |
| **Creation** | `socket = ("10.0.0.1", 443)` | Standard tuple definition. |
| **Single Element** | `single = ("10.0.0.1",)` | Trailing comma is **REQUIRED** for 1 element. |
| **Unpacking** | `ip, port = socket` | Extracts items into separate variables. |
| **Implicit Packing** | `a = 1, 2, 3` | Evaluates right side as a tuple `(1, 2, 3)`. |
| **Concatenation** | `tup1 + tup2` | Creates a completely new tuple. |
| **List Conversion**| `list(socket)` | Converts to a list (creates new memory `id`). |
| **Immutability** | `socket[1] = 80` | **FATAL `TypeError`**. Cannot mutate a tuple. |

### Sets
Sets are unordered collections of **unique** elements. Used for $O(1)$ fast lookups and deduplication.

| Operation / Method | Syntax Example | Description |
| :--- | :--- | :--- |
| **Creation (Empty)** | `ips = set()` | Creates an empty set (Note: `{}` creates a dictionary). |
| **Creation (Values)**| `ips = {"1.1.1.1", "8.8.8.8"}` | Creates a set with initial values. |
| **Deduplication** | `ips = set(["a", "a", "b"])` | Converts a list to a set, wiping out duplicates. |
| **Add Item** | `ips.add("10.0.0.5")` | Adds a single item to the set. |
| **Update Items** | `ips.update(["a", "b"])` | Adds multiple items from a list/iterable. |
| **Remove (Safe)** | `ips.discard("10.0.0.5")` | Removes item. Does nothing if item is not found. |
| **Remove (Unsafe)**| `ips.remove("10.0.0.5")` | Removes item. **FATAL `KeyError`** if not found. |
| **Pop** | `ips.pop()` | Removes and returns a **random** element. |
| **Clear** | `ips.clear()` | Wipes all elements from the set. |
| **Intersection** | `a & b` or `a.intersection(b)` | Items present in **both** sets. |
| **Union** | `a \| b` or `a.union(b)` | Items present in **either** set. |
| **Difference** | `a - b` or `a.difference(b)` | Items in A that are **not** in B. |
| **Sym Difference**| `a ^ b` or `a.symmetric_difference(b)`| Items in exactly ONE set, but not both. |
| **Subset Check** | `set_a.issubset(set_b)` | Returns `True` if all of A is in B. |
| **Superset Check** | `set_a.issuperset(set_b)` | Returns `True` if A contains all of B. |
| **Disjoint Check** | `set_a.isdisjoint(set_b)` | Returns `True` if sets have 0 common items. |

## 3. Functions & Scope

| Concept | Syntax Example | Description |
| :--- | :--- | :--- |
| **Definition** | `def check_health():` | Declares a new reusable function. |
| **Parameters** | `def check_health(ip_addr):` | Function accepts input arguments. |
| **Type Hints** | `def check_health(ip: str) -> bool:` | PEP 484 hints (documentation only). |
| **Defaults** | `def scan(port: int = 80):` | Fallback value if argument is omitted. |
| **`*args`** | `def block(*ips):` | Packs infinite positional args into a Tuple. |
| **`**kwargs`** | `def build(**specs):` | Packs infinite named args into a Dict. |
| **Return** | `return True` | Exits the function and passes data back. |
| **Multiple Return** | `return status, ip` | Returns a Tuple `(status, ip)` automatically. |
| **Global Scope** | `GLOBAL_VAR = "PROD"` | Defined outside; visible everywhere. |
| **Local Scope** | `local_var = 123` | Defined inside; destroyed when function ends. |
| **Callbacks** | `run_job(notify_func)` | Passing a function as a parameter. |


```python
def check_capacity(used: float, total: float = 100.0) -> str:
    """Evaluates utilization and returns a severity string."""
    pct = (used / total) * 100
    if pct > 90.0:
        return "CRITICAL"
    return "OK"

# Calling the function
state = check_capacity(95.5)  # Uses default total=100.0
```
