import sys
import time
from cli_builder import parse_arguments
from config import load_config
from logger import setup_logging
from orchestrator_core import run_audit_cycle, display_summary

def run_watchtower() -> int:
    print("WATCHTOWER RUN")
    args = parse_arguments()

    if not args.check and not args.daemon:
        args.check = True
    logger = setup_logging()
    logger.info("Initializing Watchtower Operation Suite...")
    logger.info(f"Execution Mode: {'DAEMON' if args.daemon else 'ONE-SHOT AUDIT'}")
    logger.info(f"Automated Self-Healing: {'ENABLED' if args.heal else 'DISABLED'}")
    logger.info(f"Dry-Run Simulation: {'ENABLED' if args.dry_run else 'DISABLED'}")

    config = load_config(args.config)
    agent_name = config.get("agent_name", "watchtower-agen")
    endpoints = config.get("endpoints", [])
    logger.info(f"Agent '{agent_name}' monitoring {len(endpoints)} endpoints...")

    if args.check:
        summary = run_audit_cycle(
            endpoints,
            timeout_sec=args.timeout,
            enable_heal=args.heal,
            dry_run=args.dry_run,
            logger=logger
        )
        display_summary(summary, args.format)

        if summary["degraded_count"] == 0:
            logger.info("Audit PASSED: All gateways healthy (Exit Code: 0)")
            return 0
        else:
            logger.error(f"Audit FAILED: {summary["degraded_count"]} degraded gateway(s) (Exit Code: 1)")
            return 1

    if args.daemon:
        logger.info(f"Starting Watchtower daemon (polling interval: {args.interval}s). Press Ctrl+C to stop.")
        cycle_num = 1
        try:
            while True:
                logger.info(f"--- Starting Audit Cycle #{cycle_num} ---")
                summary = run_audit_cycle(
                    endpoints,
                    timeout_sec=args.timeout,
                    enable_heal=args.heal,
                    dry_run=args.dry_run,
                    logger=logger
                )
                display_summary(summary, args.format)
                cycle_num += 1
                logger.info(f"Sleeeping for {args.interval} seconds untill next cycle...")
                time.sleep(args.interval)
        except KeyboardInterrupt:
            logger.info("\nReceived SIGINT (Ctrl+C). Terminating watchtower daemon cleanly")
            return 0
    # return 0


if __name__ == "__main__":
    sys.exit(run_watchtower())