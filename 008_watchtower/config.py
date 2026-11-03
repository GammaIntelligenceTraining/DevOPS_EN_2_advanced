import os
import sys
import yaml

def load_config(
    config_path: str = "config.yaml"
) -> dict:
    if not os.path.exists(config_path):
        print(f"[CRITICAL] Configuration file {config_path} is missing", file=sys.stderr)
        sys.exit(1)
    try:
        with open(config_path, "r", encoding="utf8") as f:
            config = yaml.safe_load(f)
        if not isinstance(config, dict):
            print(f"[CRITICAL] Configuration in '{config_path}': YAML mapping/dictionarty expected", file=sys.stderr)
            sys.exit(2)
        return config

    except yaml.YAMLError as exc:
        print(f"[CRITICAL] YAML syntax error in '{config_path}': {exc}", file=sys.stderr)
        sys.exit(2)


if __name__ == "__main__":
    test_path = sys.argv[1] if len(sys.argv) > 1 else "config.yaml"
    data = load_config(test_path)
    endpoints = data.get("endpoints", [])
    print(f"[OK] Agent: {data.get('agent_name', 'unknown')}")
    print(f"[OK] Timeout: {data.get('timeout_sec', 3)}s")
    print(f"[OK] Endpoints loaded: {len(endpoints)}")
    for ep in endpoints:
        print(f"    - {ep.get('name')}: {ep.get('url')}")