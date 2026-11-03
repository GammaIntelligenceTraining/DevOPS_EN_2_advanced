import time
import sys
import logging
import subprocess
from typing import List, Dict, Any, Optional


def execute_recovery_command(
    command_args: List[str],
    timeout_sec: float = 10.0,
    logger: Optional[logging.Logger] = None
) -> Dict[str, Any]:
    result = {
        "returncode": -1,
        "stdout": "",
        "stderr": "",
        "success": False
    }
    try:
        proc = subprocess.run(
            command_args,
            capture_output=True,
            text=True,
            timeout=timeout_sec
        )
        result['returncode'] = proc.returncode
        result['stdout'] = proc.stdout.strip()
        result["stderr"] = proc.stderr.strip()
        result["success"] = proc.check_returncode()
    except subprocess.TimeoutExpired:
        if logger:
            logger.error(f"Remediation command timed out after {timeout_sec}s: {' '.join(command_args)}")
    except Exception as exc:
        if logger:
            logger.error(f"Failed to execute remediation command: {exc}")

    return result


def remediate_service_with_circuit_breaker(
        target: Dict[str, Any],
        max_retries: int = 3,
        cooldown_sec: float = 2.0,
        logger: Optional[logging.Logger] = None
) -> bool:
    # ['/usr/bin/sytemctl', 'restart', 'nginx']
    name = target.get("name", "Unknown Service")
    cmd = target.get("remediation_args", [sys.executable, "-c", "print('Service cycled successfully.')"])

    if logger:
        logger.warning(f"Initiating bounded recovery for '{name}' (Max retries: {max_retries})...")

    for attempt in range(1, max_retries + 1):
        if logger:
            logger.info(f"Remediation attempt {attempt}/{max_retries} for '{name}'...")

        res = execute_recovery_command(cmd, logger=logger)

        time.sleep(cooldown_sec)

        # prober.py in real life
        target["mock_failure"] = False
        is_now_healthy = not target.get("mock_failure", False)

        if is_now_healthy:
            if logger:
                logger.info(f"SELF-HEALING SUCCESS: '{name}' came healthy on attempt {attempt}/{max_retries}")
            return True

        if logger:
            logger.warning(f"Attempt {attempt} did not resolve failure for '{name}'. Retrying...")
    if logger:
        logger.critical(
            f"CIRCUIT BREAKER TRIPPED for '{name}'! Service failed to recover after {max_retries} attempts." \
            f"Halting automated healing to protect system stability!"
        )
    return False