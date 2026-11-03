import sys
import logging


def setup_logging(
        log_path: str = "watchtower_audit.log",
        level: int = logging.DEBUG
) -> logging.Logger:
    logger = logging.getLogger("watchtower")
    logger.setLevel(level)
    logger.handlers.clear()

    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setLevel(logging.INFO)
    console_formatter = logging.Formatter("[%(levelname)s] %(message)s")
    console_handler.setFormatter(console_formatter)

    file_handler = logging.FileHandler(log_path, mode="a", encoding="utf8")
    file_handler.setLevel(logging.DEBUG)
    file_formatter = logging.Formatter("%(asctime)s [%(levelname)s] %(message)s")
    file_handler.setFormatter(file_formatter)

    logger.addHandler(console_handler)
    logger.addHandler(file_handler)
    return logger


if __name__ == '__main__':
    log = setup_logging("test_watchtower.log")
    log.debug("DEBUG message")
    log.info("INFO message")
    log.warning("WARNING message")
    log.error("ERROR message")
    log.critical("CRITICAL message")