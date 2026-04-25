import logging
from pathlib import Path


def setup_logger(log_path: Path, log_level: str = "INFO"):
    """
    Configure root logger.

    English:
    Set global logging configuration.

    日本語：
    グローバルログ設定を行う。
    """

    level = getattr(logging, log_level.upper(), logging.INFO)

    if log_path.is_dir() or str(log_path).endswith("/"):
        log_path.mkdir(parents=True, exist_ok=True)
        log_file = log_path / "app.log"
    else:
        log_path.parent.mkdir(parents=True, exist_ok=True)
        log_file = log_path

    logging.basicConfig(
        level = level,
        format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
        handlers=[
            logging.StreamHandler(),           # console output
            logging.FileHandler(log_file)     # file output
        ]
    )

    


def get_logger(name: str) -> logging.Logger:
    """
    Get a logger instance.

    English:
    Returns a named logger.

    日本語：
    名前付きロガーを取得する。
    """
    return logging.getLogger(name)
