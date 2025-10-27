"""Module provides configurations for the API"""
import logging
from pathlib import Path
from rich.logging import RichHandler


VERSION_FILE = Path(__file__).parent.parent / "VERSION"

logging.basicConfig(
    level="NOTSET", format="%(levelname)s: %(message)s", handlers=[RichHandler()]
    )
log = logging.getLogger("rich")


try:
    with open(file=VERSION_FILE, mode="r", encoding="utf-8") as version_file:
        VERSION = version_file.readline().strip()
except FileNotFoundError as e:
    log.error("Version file not found : %s", str(e))
    VERSION = ""
except PermissionError as e:
    log.error("Permission Denied to open Version file : %s", str(e))
    VERSION = ""
