import os
from datetime import datetime
import numpy as np

"""
defining common constant variable for training pipeline
"""

def get_current_time_stamp():
    return f"{datetime.now().strftime('%Y-%m-%d-%H-%M-%S')}"

def get_log_file_name():
    return f"log_{get_current_time_stamp()}.log"


ROOT_DIR = os.getcwd()  # to get current directory

CONFIG_DIR = "config"
CONFIG_FILE_NAME = "config.yaml"
CONFIG_FILE_PATH = os.path.join(ROOT_DIR,CONFIG_DIR,CONFIG_FILE_NAME)

CURRENT_TIME_STAMP = get_current_time_stamp()


## Common variables
TARGET_COLUMN = "target"
PIPELINE_NAME: str = "HeartDiseasePrediction"
ARTIFACT_DIR_NAME: str = "Artifacts"


FILE_NAME: str = "heart.csv"

TRAIN_FILE_NAME: str = "train.csv"
TEST_FILE_NAME: str = "test.csv"

SCHEMA_FILE_PATH = os.path.join("data_schema", "schema.yaml")

SAVED_MODEL_DIR =os.path.join("saved_models")
MODEL_FILE_NAME = "model.pkl"


## LOG Related variables
LOG_DIR="logs"
LOG_FILE_NAME = get_log_file_name()
LOG_FILE_PATH = os.path.join(ROOT_DIR,LOG_DIR,LOG_FILE_NAME)
LOG_FILE_FORMAT = "[%(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s"

# Training Pipeline related variable
TRAINING_PIPELINE_CONFIG_KEY = 'training_pipeline_config'
TRAINING_PIPELINE_ARTIFACT_DIR_KEY = 'artifact_dir'
TRAINING_PIPELINE_NAME_KEY = 'pipeline_name'

FILE_PATH = "Data\heart.csv"

## Data Ingestion ralated variables
DATA_INGESTION_ARTIFACT_DIR = 'data_ingetsion'
# DATA_INGESTION_CONFIG_KEY = 'data_ingestion_config'
# DATA_INGESTION_INPUT_FILE_PATH = 'dataset_download_url'
DATA_INGESTION_RAW_DATA_DIR_KEY = 'raw_data_dir'
#DATA_INGESTION_TGZ_DOWNLOAD_DIR_KEY = 'tgz_download_dir'
DATA_INGESTION_INGESTED_DIR_NAME_KEY = 'ingested_dir'
# DATA_INGESTION_TRAIN_DIR_KEY = 'ingested_train_dir'
# DATA_INGESTION_TEST_DIR_KEY = 'ingested_test_dir'
DATA_INGESTION_TRAIN_TEST_SPLIT_RATIO = 0.2


## Data Validation related Varialbels
DATA_VALIDATION_DIR_NAME: str = "data_validation"
DATA_VALIDATION_VALID_DIR: str = "validated"
DATA_VALIDATION_INVALID_DIR: str = "invalid"
DATA_VALIDATION_DRIFT_REPORT_DIR: str = "drift_report"
DATA_VALIDATION_DRIFT_REPORT_FILE_NAME:str = "report.yaml"




"""
Data Transformation related constant start with DATA_TRANSFORMATION VAR NAME
"""
DATA_TRANSFORMATION_DIR_NAME: str = "data_transformation"
DATA_TRANSFORMATION_TRANSFORMED_DATA_DIR: str = "transformed"
DATA_TRANSFORMATION_TRANSFORMED_OBJECT_DIR: str = "transformed_object"
PREPROCESSING_OBJECT_FILE_NAME = "preprocessing.pkl"

## kkn imputer to replace nan values
DATA_TRANSFORMATION_IMPUTER_PARAMS: dict = {
    "missing_values": np.nan,
    "n_neighbors": 3,
    "weights": "uniform",
}
DATA_TRANSFORMATION_TRAIN_FILE_PATH: str = "train.npy"

DATA_TRANSFORMATION_TEST_FILE_PATH: str = "test.npy"




"""
Model Trainer ralated constant start with MODE TRAINER VAR NAME
"""

MODEL_TRAINER_DIR_NAME: str = "model_trainer"
# MODEL_TRAINER_TRAINED_MODEL_DIR: str = "trained_model"
MODEL_TRAINER_TRAINED_MODEL_NAME: str = "model.pkl"
MODEL_TRAINER_EXPECTED_SCORE: float = 0.6
MODEL_TRAINER_OVER_FIITING_UNDER_FITTING_THRESHOLD: float = 0.05

TRAINING_BUCKET_NAME = "heartdisease"









