import time
import logging
from typing import Optional
import requests

def probe_gateway(
    name: str,
    url: str,
    timeout: float = 3,
    logger: Optional[logging.Logger] = None
) -> dict:

    telemetry = {
        "name": name,
        "url": url,
        "status_code": None,
        "latency_ms": None,
        "is_healthy": False,
        "error": None
    }

    start_time = time.time()
    try:
        res = requests.get(url, timeout=timeout)
        elapsed_ms = round((time.time() - start_time) * 1000, 2)
        telemetry["latency_ms"] = elapsed_ms
        telemetry["status_code"] = res.status_code

        if res.status_code == 200:
            telemetry["is_healthy"] = True
            if logger:
                logger.info(f"Gateway UP: '{name}' (Status: 200, Latency: {elapsed_ms})")
        else:
            telemetry["error"] = f"HTTP {res.status_code}"
            if logger:
                logger.warning(f"Gateway DEGRADED: '{name}' returned status {res.status_code}")
    except requests.exceptions.Timeout:
        telemetry["error"] = f"Timed out after {timeout}s"
        if logger:
            logger.error(f"Gateway TIMEOUT: '{name}' connection refused")
    except requests.exceptions.ConnectionError:
        telemetry["error"] = "Connection refused or DNS failure"
        if logger:
            logger.error(f"Gateway FAILED: '{name}' connection refused")
    except requests.exceptions.RequestException as exc:
        telemetry["error"] = str(exc)
        if logger:
            logger.error(f"Gateway ERROR: '{name}' network error: {exc}")

    return telemetry    

if __name__ == "__main__":
    from pprint import pp
    from logger import setup_logging
    log = setup_logging("prober_audit.log")
    test_result = probe_gateway("GitHub API", "https://api.github.com", timeout=3.0, logger=log)
    pp(test_result)