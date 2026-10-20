# Python Module 7 Cheat Sheet: Production CLI Utilities & YAML Configuration

## 1. Standard Streams & Exit Codes (`sys`)

| Stream / Call | Description | Syntax Example |
| :--- | :--- | :--- |
| `sys.stdout` | Standard output stream (File descriptor 1). Clean data payloads. | `sys.stdout.write("result\n")` |
| `sys.stderr` | Standard error stream (File descriptor 2). Logs and alerts. | `sys.stderr.write("[ERROR] failed\n")` |
| `sys.exit(0)` | Clean, successful process termination. | `sys.exit(0)` |
| `sys.exit(1)` | Non-zero exit code signaling general operational failure. | `sys.exit(1)` |
| `sys.exit(2)` | Standard exit code for command-line syntax or argument errors. | `sys.exit(2)` |

---

## 2. Core `argparse` Quick Reference

```python
import argparse

parser = argparse.ArgumentParser(
    prog="tool_name",
    description="Tool description displayed in help banner",
    epilog="Footer text or usage examples"
)
```

| Method / Parameter | Syntax Example | Purpose |
| :--- | :--- | :--- |
| **Positional Argument** | `parser.add_argument("host")` | Mandatory parameter without dashes. |
| **Optional Flag** | `parser.add_argument("-e", "--env")` | Flag with short (`-e`) and long (`--env`) forms. |
| **Default Value** | `default="staging"` | Fallback value if optional flag is omitted. |
| **Type Conversion** | `type=int`, `type=float` | Automatically converts string input to specified type. |
| **Restricted Choices** | `choices=["dev", "prod"]` | Rejects any value not present in the allowed list. |
| **Boolean Flag** | `action="store_true"` | Sets variable to `True` if present, `False` if omitted. |
| **Mandatory Flag** | `required=True` | Forces an optional-style flag (`--token`) to be required. |
| **Help Description** | `help="Help text for option"` | Documentation string displayed in `--help` / `-h`. |
| **Parse Invocations** | `args = parser.parse_args()` | Parses arguments and returns `Namespace` object. |

---

## 3. Subcommands Quick Reference (`add_subparsers`)

```python
# 1. Initialize subparser engine
subparsers = parser.add_subparsers(dest="command", required=True)

# 2. Add individual subcommands (verbs)
parser_start = subparsers.add_parser("start", help="Start service")
parser_start.add_argument("service_name")

parser_stop = subparsers.add_parser("stop", help="Stop service")
parser_stop.add_argument("service_name")
parser_stop.add_argument("--force", action="store_true")

# 3. Branching on command execution
args = parser.parse_args()
if args.command == "start":
    print(f"Starting {args.service_name}")
```

---

## 4. PyYAML Configuration Management Matrix

```python
import yaml
```

| Operation | Syntax Example | Description |
| :--- | :--- | :--- |
| **Safe Deserialization** | `data = yaml.safe_load(f)` | Parses YAML string or file object into Python dictionary/list. |
| **File Reading** | `with open("cfg.yaml") as f:`<br>`data = yaml.safe_load(f)` | Idiomatic pattern for loading YAML manifests from disk. |
| **Serialization (Dump)** | `out = yaml.dump(data)` | Converts Python dictionary into a formatted YAML string. |
| **File Export** | `with open("out.yaml", "w") as f:`<br>`yaml.dump(data, f)` | Writes Python dictionary directly to a YAML file on disk. |
| **Formatting: Flow Style**| `default_flow_style=False` | Enforces multiline block format instead of inline `{a: 1}` format. |
| **Formatting: Key Order** | `sort_keys=False` | Preserves original insertion order of dictionary keys. |

---

## 5. YAML Syntax Quick Reference

| YAML Construct | Syntax Example | Python Data Mapping |
| :--- | :--- | :--- |
| **Key-Value Pair** | `replicas: 3` | `dict` (`{"replicas": 3}`) |
| **String Scalar** | `app: "auth-gateway"` | `str` (quotes optional unless containing special characters) |
| **Boolean** | `enabled: true` | `bool` (`True`/`False`, lowercase preferred) |
| **Null Value** | `cache: null` or `cache: ~` | `None` |
| **Block List** | `ports:`<br>`  - 80`<br>`  - 443` | `list` (`[80, 443]`) |
| **Inline List** | `ports: [80, 443]` | `list` (`[80, 443]`) |
| **Nested Mapping** | `db:`<br>`  host: "db.internal"` | `dict` inside `dict` (spaces only, no tabs) |
| **List of Objects** | `services:`<br>`  - name: "web"`<br>`    port: 80` | `list` of `dict` (standard Kubernetes/Compose format) |
| **Literal String** | `script: \|`<br>`  echo hello` | Multiline `str` preserving exact line breaks |
| **Folded String** | `desc: >`<br>`  long line` | Multiline `str` folding line breaks into spaces |

---

## 6. Production CLI Template Pattern

```python
import sys
import os
import argparse
import yaml

def main():
    parser = argparse.ArgumentParser(prog="opsctl", description="DevOps Node Controller")
    parser.add_argument("-c", "--config", default="config.yaml", help="Path to YAML config")
    parser.add_argument("--timeout", type=int, help="Override timeout seconds")
    args = parser.parse_args()

    if not os.path.exists(args.config):
        sys.stderr.write(f"Error: Configuration file '{args.config}' not found.\n")
        sys.exit(1)

    try:
        with open(args.config, "r", encoding="utf-8") as f:
            config = yaml.safe_load(f)
    except yaml.YAMLError as exc:
        sys.stderr.write(f"Error: Malformed YAML syntax: {exc}\n")
        sys.exit(2)

    # Layer CLI overrides on top of config defaults
    if args.timeout is not None:
        config["timeout"] = args.timeout

    sys.stdout.write(f"Execution succeeded with timeout: {config.get('timeout', 30)}s\n")
    sys.exit(0)

if __name__ == "__main__":
    main()
```
