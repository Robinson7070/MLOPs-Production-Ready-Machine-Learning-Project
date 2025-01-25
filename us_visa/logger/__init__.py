import logging
import os

from from_root import from_root
from datetime import datetime

LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

log_dir = 'logs'

root_dir = os.getcwd()  # Gets the directory where the script is run
logs_path = os.path.join(root_dir, log_dir, LOG_FILE)


os.makedirs(log_dir, exist_ok=True)


logging.basicConfig(
    filename=logs_path,
    format="[ %(asctime)s ] %(name)s - %(levelname)s - %(message)s",
    level=logging.DEBUG,
)