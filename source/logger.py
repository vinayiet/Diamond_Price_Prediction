import logging
import os 
from datetime import datetime


LOG_FILE=F'{datetime.now().strftime("%Y-%m-%d")}.log'
log_path = os.path.join(os.getcwd(), 'logs', LOG_FILE)
os.makedirs(os.path.dirname(log_path), exist_ok=True)

LOF_FILE_PATH = os.path.join(log_path, LOG_FILE)


logging.basicConfig(
    filename=LOG_FILE,
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level = logging.INFO   

)
