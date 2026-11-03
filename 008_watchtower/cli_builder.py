import argparse


def parse_arguments() -> argparse.Namespace:

    parser = argparse.ArgumentParser(
        prog="watchtower",
        description="Watchtower: Autonomou Cluster Gateway & Systemd Healing Agent"
    )

    mode_group = parser.add_mutually_exclusive_group()
    mode_group.add_argument(
        "--check",
        action="store_true",
        help="Run a single audit pass and exit with POSIX code (0=healthy, 1=degraded)"
    )

    mode_group.add_argument(
        "--daemon",
        action="store_true",
        help="Run continuously as a backdround monitoring daemon."
    )

    parser.add_argument(
        "--config",
        default="config.yaml",
        help="Path to YAML configuration manifest (default: config.yaml)"
    )

    parser.add_argument(
        "--interval",
        type=int,
        default=10,
        help="Polling interval in seconds for daemon mode (default: 10)"
    )

    parser.add_argument(
        "--timeout",
        type=float,
        default="3.0",
        help="Timeout in seconds"
    )

    parser.add_argument(
        "--heal",
        action="store_true",
        help="Enable automated self-healing remediation on failure"
    )

    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Simulate the remediation without executing host commands"
    )

    parser.add_argument(
        "--format",
        choices=["text", "json"],
        default="text",
        help="Telemetry output format (default: text)"
    )

    return parser.parse_args()
