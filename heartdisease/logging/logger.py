import logging
import os
from datetime import datetime
from heartdisease.constants import ROOT_DIR,LOG_DIR, LOG_FILE_NAME,LOG_FILE_PATH, LOG_FILE_FORMAT



## Making Logging Directory

os.makedirs(LOG_FILE_PATH,exist_ok=True)

LOG_FILE = os.path.join(LOG_FILE_PATH,LOG_FILE_NAME)

logging.basicConfig(
    filemode='w',
    filename=LOG_FILE,
    format=LOG_FILE_FORMAT,
    level=logging.INFO
)

# if __name__ == "__main__":
#     logging.info("Logging has started")





