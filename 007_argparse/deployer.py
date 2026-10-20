import argparse
import sys
import os
import yaml

parser = argparse.ArgumentParser(description="Production Deployer with YAML Config Layering")
parser.add_argument("-c", "--config", default="deploy.yaml", help="Path to YAML configuration")
parser.add_argument("--replicas", type=int, help="Override worker replica count")
parser.add_argument("--env", choices=["dev", "prod", "staging"], help="Override environment tier")

args = parser.parse_args()

if not os.path.exists(args.config):
    sys.stderr.write(f"[ERROR] Specified configuration file: '{args.config}' not found!\n")
    sys.exit(1)

try:
    with open(args.config, 'r') as f:
        manifest = yaml.safe_load(f)
except yaml.YAMLError as e:
    sys.stderr.write(f"[FATAL] Syntax error while parsing YAML file: {e}\n")
    sys.exit(2)

if args.replicas is not None:
    print(f"Overriding YAML replicas ({manifest.get('replicas')}) with CLI flag: {args.replicas}")
    manifest['replicas'] = args.replicas

if args.env is not None:
    print(f"Overriding YAML env ({manifest.get('environment')}) with CLI flag: {args.env}")
    manifest['environment'] = args.env


print("\n--- Final Deployment State ---")
print(f"App Name    : {manifest.get('app_name', 'unknown')}")
print(f"Environment : {manifest.get('environment')}")
print(f"Worker Count: {manifest.get('replicas')}")

sys.exit(0)