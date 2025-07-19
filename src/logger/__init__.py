import logging
import logging.config
import yaml
import os
from datetime import datetime
from from_root import from_root 

LOG_DIR = 'logs'
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

# Create logs directory
log_dir_path = os.path.join(from_root(), LOG_DIR)
os.makedirs(log_dir_path, exist_ok=True)

# Full path to dynamic log file
log_file_path = os.path.join(log_dir_path, LOG_FILE)

def configure_logger():
    with open(from_root("logging_config.yaml"), "r") as f:
        config = yaml.safe_load(f)

    # Inject dynamic log file path
    config['handlers']['rotating_file_handler']['filename'] = log_file_path
    logging.config.dictConfig(config)

# Run configuration once
configure_logger()

# Expose a named logger
logger = logging.getLogger(__name__)
