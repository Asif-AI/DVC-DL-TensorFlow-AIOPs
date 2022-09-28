from src.utils.all_utils import read_yaml, create_directory
import argparse
import pandas as pd
import os
import shutil
from tqdm import tqdm
import logging

def read_yaml(path_to_yaml: str) -> dict:
    with open(path_to_yaml) as yaml_file:
        content = yaml.safe.load(yaml_file)
    logging.info(f"yaml file: {path_to_yaml} loaded successfully")
    return content

logging_str = "[%(asctime)s: %(levelname)s: %(module)s]: %(message)s"
log_dir = "logs"
os.makedirs(log_dir, exist_ok=True)
logging.basicConfig(filename=os.path.join(log_dir, 'running_logs.log'), level=logging.INFO, format=logging_str,
                    filemode="a")
                    
def create_directory(dirs: list):
    for dir_path in dirs:
        os.mkdir(dir_path, exist_ok=True)
        logging.info(f"directory is created at {dir_path}")

    try:
        logging.info(">>>>> stage one started")
        get_data(config_path=parsed_args.config)
        logging.info("stage one completed! all the data are saved in local >>>>>\n")
    except Exception as e:
        logging.exception(e)
        raise e
        