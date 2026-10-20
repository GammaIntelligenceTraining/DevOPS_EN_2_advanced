#!/usr/bin/env python3
"""
==============================================================================
Module 7: Production CLI Utilities & Configuration Management (argparse + YAML)
==============================================================================

Overview:
In systems engineering and DevOps automation, scripts rarely run with hardcoded
variables or interactive input() prompts. Real automation runs non-interactively
inside CI/CD pipelines, cron jobs, and orchestrators. 

This runnable reference script covers the engineering foundations required to
author production-ready command-line utilities and configuration parsers:
1. Standard Streams: sys.stdout, sys.stderr, and POSIX exit code contracts.
2. Argument Parsing: Declarative CLI architecture using the argparse module.
3. Argument Types & Validation: Positional parameters, optional flags, type conversion,
   and restricted choices.
4. Boolean Toggles: Flag switches using action="store_true".
5. Subcommands: Building multi-command routers (e.g., opsctl server start).
6. Configuration Management: Parsing and generating YAML manifests with PyYAML.
7. Configuration Layering: Overriding static YAML defaults with dynamic CLI flags.

Requirements:
    pip install pyyaml

Execution:
    Run directly in your terminal:
    - Windows (PowerShell): python handout.py
    - macOS / Linux       : python3 handout.py
==============================================================================
"""

import sys
import os
import argparse
import yaml


# ==============================================================================
# SECTION 1: Standard Streams & Exit Code Contracts
# ==============================================================================
# Operating systems manage I/O through three standard file descriptor streams:
# - Stream 0 (stdin): Standard input.
# - Stream 1 (stdout): Standard operational output and data payloads.
# - Stream 2 (stderr): Diagnostic messages, warnings, and errors.
#
# Directing errors to stderr ensures that downstream pipeline tools expecting
# clean data on stdout (such as JSON or CSV) do not fail when errors occur.

print("=" * 70)
print("SECTION 1: Standard Streams & Exit Code Contracts")
print("=" * 70)

# Writing explicitly to stdout (Stream 1)
# Note: unlike print(), sys.stdout.write() does not automatically add a newline.
sys.stdout.write("Status: Operational data emitted to stdout (Stream 1).\n")

# Writing explicitly to stderr (Stream 2)
# When executing './script.py > output.txt', this message still prints to the console.
sys.stderr.write("[DIAGNOSTIC] Warning or error output emitted to stderr (Stream 2).\n")

# Process Exit Codes:
# Every process signals termination state via an integer exit code (0 to 255).
# - Exit Code 0: Clean, successful termination.
# - Exit Code 1-255: Failure or syntax violation.
# CI/CD runners check this code to determine whether to pass or fail a build step.
#
# Example function demonstrating conditional exit codes:
def simulate_threshold_check(cpu_utilization: float):
    """Evaluates host utilization and demonstrates clean exit signaling."""
    if cpu_utilization > 90.0:
        sys.stderr.write(f"[CRITICAL] CPU breach ({cpu_utilization}%). Pipeline halted.\n")
        # In a real CLI script, you would terminate immediately with sys.exit(1)
        # sys.exit(1)
        return 1
    
    sys.stdout.write(f"[OK] CPU utilization normal ({cpu_utilization}%).\n")
    return 0

simulate_threshold_check(74.5)


# ==============================================================================
# SECTION 2: Core argparse - Positional Arguments & Optional Flags
# ==============================================================================
# The argparse module is part of Python's standard library. It inspects command-line
# arguments, validates types, enforces mandatory inputs, and generates --help menus.

print("\n" + "=" * 70)
print("SECTION 2: Core argparse - Positional Arguments & Optional Flags")
print("=" * 70)

# 1. Initialize the ArgumentParser
# prog defines the tool name shown in usage syntax.
# description provides an overview of the tool.
demo_parser = argparse.ArgumentParser(
    prog="deployctl",
    description="Automated Service Deployment & Provisioning Controller",
    epilog="Example: deployctl web-01.internal --environment prod --retries 3"
)

# 2. Add Positional Arguments
# Positional arguments do NOT have leading dashes ('-').
# They are mandatory by default. If omitted, argparse displays an error and exits.
demo_parser.add_argument(
    "target_host",
    help="Target server hostname or IP address to provision"
)

# 3. Add Optional Arguments (Flags)
# Optional flags begin with '-' (short form) or '--' (long form).
# They can appear in any order and accept fallback default values.
demo_parser.add_argument(
    "-e", "--environment",
    default="staging",
    choices=["dev", "staging", "prod"],
    help="Target infrastructure tier (default: staging)"
)

# 4. Type Enforcement & Conversion
# The type= parameter automatically converts the input string to the specified type.
# If conversion fails (e.g. user passes 'three' instead of 3), argparse halts execution.
demo_parser.add_argument(
    "-r", "--retries",
    type=int,
    default=1,
    help="Maximum connection retry attempts (default: 1)"
)

# We can simulate parsing specific command-line arguments using a test list
# In actual scripts, you simply call parser.parse_args() without arguments.
test_cli_args = ["web-01.internal", "--environment", "prod", "--retries", "3"]
parsed_demo = demo_parser.parse_args(test_cli_args)

print("Parsed Argument Values:")
print(f"  Target Host   : {parsed_demo.target_host}")
print(f"  Environment   : {parsed_demo.environment}")
print(f"  Retry Attempts: {parsed_demo.retries} (Type: {type(parsed_demo.retries).__name__})")


# ==============================================================================
# SECTION 3: Boolean Switches & Custom Flag Actions
# ==============================================================================
# In CLI utilities, some flags do not accept a value; their mere presence toggles
# an option on or off (e.g., --verbose, --dry-run, --force).
#
# Use action="store_true" for boolean flags:
# - If the flag is omitted: variable is set to False.
# - If the flag is provided: variable is set to True.

print("\n" + "=" * 70)
print("SECTION 3: Boolean Switches & Flag Actions")
print("=" * 70)

toggle_parser = argparse.ArgumentParser(prog="audit_agent")

toggle_parser.add_argument(
    "--dry-run",
    action="store_true",
    help="Simulate execution without modifying real infrastructure"
)

toggle_parser.add_argument(
    "-v", "--verbose",
    action="store_true",
    help="Display detailed diagnostic logs during execution"
)

# Test 1: Flag provided
args_with_flags = toggle_parser.parse_args(["--dry-run", "-v"])
print("Test 1 (Flags Provided):")
print(f"  dry_run : {args_with_flags.dry_run}")
print(f"  verbose : {args_with_flags.verbose}")

# Test 2: Flags omitted
args_omitted = toggle_parser.parse_args([])
print("\nTest 2 (Flags Omitted):")
print(f"  dry_run : {args_omitted.dry_run}")
print(f"  verbose : {args_omitted.verbose}")


# ==============================================================================
# SECTION 4: Multi-Command Architecture (Subparsers)
# ==============================================================================
# Enterprise tools like docker, git, and kubectl organize functionality into verbs
# called subcommands (e.g., 'docker run', 'docker build', 'git commit').
# In argparse, this is implemented using add_subparsers().

print("\n" + "=" * 70)
print("SECTION 4: Multi-Command Architecture (Subparsers)")
print("=" * 70)

router_parser = argparse.ArgumentParser(prog="clusterctl", description="Cluster Management Utility")

# Initialize the subparser collection
# dest="subcommand" stores which subcommand the user executed
subparsers = router_parser.add_subparsers(
    dest="subcommand",
    required=True,
    help="Action to perform on the cluster"
)

# Subcommand 1: 'scale'
parser_scale = subparsers.add_parser("scale", help="Scale cluster worker pool")
parser_scale.add_argument("cluster_id", help="Target cluster identifier")
parser_scale.add_argument("--replicas", type=int, required=True, help="Target worker node count")

# Subcommand 2: 'drain'
parser_drain = subparsers.add_parser("drain", help="Drain nodes for maintenance")
parser_drain.add_argument("cluster_id", help="Target cluster identifier")
parser_drain.add_argument("--force", action="store_true", help="Evict pods immediately")

# Simulating execution of the 'scale' subcommand
simulated_scale_call = ["scale", "prod-cluster-us-east", "--replicas", "12"]
parsed_router = router_parser.parse_args(simulated_scale_call)

print(f"Executed Subcommand : {parsed_router.subcommand}")
print(f"Target Cluster ID   : {parsed_router.cluster_id}")
print(f"Requested Replicas  : {parsed_router.replicas}")


# ==============================================================================
# SECTION 5: Configuration Management with PyYAML
# ==============================================================================
# YAML is the primary configuration format in DevOps (Kubernetes manifests,
# Docker Compose, GitHub Actions, Ansible).
#
# Core YAML Syntax Principles:
# 1. Indentation with Spaces: YAML strictly forbids tabs (\t); use 2 spaces per level.
# 2. Key-Value Syntax: Requires a space after the colon (key: value).
# 3. Native Collections: Lists use leading dashes (- item), maps use nested indentation.
# 4. Comments: Anything after '#' is ignored (unlike JSON which forbids comments).
#
# Always use yaml.safe_load() to prevent arbitrary code execution vulnerabilities.

print("\n" + "=" * 70)
print("SECTION 5: Configuration Management with PyYAML")
print("=" * 70)

# Simulated YAML configuration document
mock_yaml_manifest = """
application:
  name: "auth-gateway"
  environment: "production"
  tier: "frontend"
scaling:
  min_replicas: 2
  max_replicas: 10
  current_replicas: 4
network:
  ingress_port: 443
  allowed_subnets:
    - "10.0.1.0/24"
    - "10.0.2.0/24"
"""

# 5.1 Safe Deserialization (yaml.safe_load)
config_dict = yaml.safe_load(mock_yaml_manifest)

print("Parsed YAML into Python Dictionary:")
print(f"  App Name        : {config_dict['application']['name']}")
print(f"  Current Replicas: {config_dict['scaling']['current_replicas']}")
print(f"  Ingress Port    : {config_dict['network']['ingress_port']}")
print(f"  Allowed Subnets : {config_dict['network']['allowed_subnets']}")

# 5.2 Mutating Configuration in Memory
config_dict['scaling']['current_replicas'] = 8
config_dict['network']['allowed_subnets'].append("10.0.3.0/24")

# 5.3 Exporting / Serializing YAML (yaml.dump)
# - sort_keys=False preserves original key insertion order.
# - default_flow_style=False enforces standard multiline block indentation.
updated_yaml = yaml.dump(config_dict, sort_keys=False, default_flow_style=False)
print("\nGenerated Mutated YAML:")
print(updated_yaml)


# ==============================================================================
# SECTION 6: Configuration Layering & Overrides
# ==============================================================================
# In production pipelines, scripts load static configuration defaults from a YAML
# file, and allow operators to override specific settings via CLI flags.

print("=" * 70)
print("SECTION 6: Configuration Layering & Overrides")
print("=" * 70)

# 1. Base configuration loaded from file
base_config = {
    "app_name": "payment-api",
    "environment": "production",
    "timeout": 30,
    "debug": False
}

# 2. Simulated CLI overrides provided by operator: --environment staging --timeout 60
simulated_cli_overrides = {
    "environment": "staging",
    "timeout": 60,
    "debug": None # None indicates the operator did not specify this flag
}

# 3. Layer CLI overrides on top of base configuration
consolidated_config = base_config.copy()
for key, val in simulated_cli_overrides.items():
    if val is not None:
        consolidated_config[key] = val

print("Base Configuration:")
print(f"  {base_config}")
print("\nFinal Consolidated Configuration (CLI Overrides Applied):")
print(f"  {consolidated_config}")
print("=" * 70)

