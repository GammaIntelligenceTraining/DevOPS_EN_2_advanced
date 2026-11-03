import sys
import time
import json
import logging
from typing import List, Dict, Any, Optional

from prober import probe_gateway
from remediator import remediate_service_with_circuit_breaker


def run_audit_cycle(
        endpoints: List[Dict[str, Any]],
        timeout_sec: float = 2.5,
        enable_heal: bool = False,
        dry_run: bool = False,
        logger: Optional[logging.Logger] = None
) -> Dict[str, Any]:
    summary = {
        "timestamp": time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime()),
        "total_targets": len(endpoints),
        "healthy_count": 0,
        "degraded_count": 0,
        "healed_count": 0,
        "telemetry": []
    }

    if logger:
        logger.info(f"Initializin audit cycle across {len(endpoints)} configured endpoints...")

    for ep in endpoints:
        name = ep.get("name", "Unknown Service")
        url = ep.get("url", "")
        telemetry = probe_gateway(name, url, timeout=timeout_sec, logger=logger)
        summary["telemetry"].append(telemetry)

        if telemetry["is_healthy"]:
            summary["healthy_count"] += 1
        else:
            summary["degraded_count"] += 1

            if enable_heal:
                healed = remediate_service_with_circuit_breaker(
                    ep,
                    max_retries=3,
                    cooldown_sec=1.0,
                    dry_run=dry_run,
                    logger=logger
                )
                if healed:
                    summary["healed_count"] += 1
                    summary["degraded_count"] -= 1
                    summary["healhty_count"] += 1

    return summary


# output_format ('text', 'json')
def display_summary(
    summary: Dict[str, Any],
    output_format: str = "text"
) -> None:
    if output_format == "json":
        print(json.dumps(summary, indent=2))
    else:
        print("\n" + "=" * 65)
        print(f"WATCHTOWER AUDIT SUMMARY ({summary["timestamp"]})")
        print("=" * 65)
        print(f"Total Targets Evaluated : {summary["total_targets"]}")
        print(f"Healthy Nodes           : {summary["healthy_count"]}")
        print(f"Degraded Nodes          : {summary["degraded_count"]}")
        print(f"Autonomously Healed     : {summary["healed_count"]}")



    # sample_nodes = [
    #     {"name": "Gateway-01", "url": "https://api.internal/v1", "is_healthy": True, "latency_ms": 42.1},
    #     {"name": "Worker-02", "url": "https://api.internal/v2", "is_healthy": False, "latency_ms": 350.8},
    #     {"name": "Auth-DB", "url": "https://auth.internal/status", "is_healthy": True, "latency_ms": 15.4},
    # ]