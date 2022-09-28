from src.utils.all_utils import read_yaml, create_directory
import argparse
import pandas as pd
import os
import shutil
from tqdm import tqdm
import logging


logging_str = "[%(asctime)s: %(levelname)s: %(module)s]: %(message)s"
log_dir = "logs"
os.makedirs(log_dir, exist_ok=True)
logging.basicConfig(filename=os.path.join(log_dir, 'running_logs.log'), level=logging.INFO, format=logging_str,
                    filemode="a")

def prepare_base_model (config_path, params_path):
    config = read_yaml(config_path)
    params = read_yaml(params_path)

    artifacts = config["artifacts"] 
    artifacts_dir = artifacts["artifacts_dir"]
    base_model_dir = artifacts["BASE_MODEL_DIR"]
    base_model_name = artifacts["BASE_MODEL_NAME"]

    base_model_dir_path = os.path.join(artifacts_dir, base_model_dir,)
    base_model_dir


    create_directory(["base_model_dir_path"])

    model = get_VGG_16_model(input_shape=params["IMAGE_SIZE"], model_path=base_model_dir_path)



  TRAINED_MODEL_DIR: model

  BASE_MODEL_NAME:  VGG16_base_model.h5
  UPDATED_BASE_MODEL_NAME:  updated_VGG16_base_model.h5
  CHECKPOINTS: checkpoints_dir
  BASE_LOG_DIR:  base_model_dir
  TENSORBOARD_ROOT_LOG_DIR:  tensorboard_log_dir
  CALLBACKS_DIR:  Callbacks_dir




if __name__ == '__main__':
    args = argparse.ArgumentParser()

    args.add_argument("--config", "-c", default="config/config.yaml")
    args.add_params("--config", "-p", default="params.yaml")

    parsed_args = args.parse_args()

    try:
        logging.info(">>>>> stage one started")
        prepare_base_model(config_path=parsed_args.config, params_path=parsed_args.params)
        logging.info("stage two completed! Base Model Created >>>>>\n")
    except Exception as e:
        logging.exception(e)
        raise e