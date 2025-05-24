import os
from datetime import datetime


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
PREPROCESSING_OBJECT_FILE_NAME = "preprocessing.pkl"



## Data Transformer ralated Variables
DATA_TRANSFORMATION_ARTIFACT_DIR = 'data_transformation'
DATA_TRANSFORMATION_CONFIG_KEY = 'data_transformation_config'
DATA_TRANSFORMATION_ADD_BEDROOM_PER_ROOM_KEY = 'add_bedroom_per_room'
DATA_TRANSFORMATION_DIR_NAME_KEY = 'transformed_dir'
DATA_TRANSFORMATION_TRAIN_DIR_NAME_KEY = 'transformed_train_dir'
DATA_TRANSFORMATION_TEST_DIR_NAME_KEY = 'transformed_test_dir'
DATA_TRANSFORMATION_PREPROCESSING_DIR_KEY = 'preprocessing_dir'
DATA_TRANSFORMATION_PREPROCESSED_FILE_NAME_KEY = 'preprocessed_object_file_name'

COLUMN_TOTAL_ROOMS = "total_rooms"
COLUMN_POPULATION = "population"
COLUMN_HOUSEHOLDS = "households"
COLUMN_TOTAL_BEDROOM = "total_bedrooms"
DATASET_SCHEMA_COLUMNS_KEY=  "columns"

NUMERICAL_COLUMN_KEY="numerical_columns"
CATEGORICAL_COLUMN_KEY = "categorical_columns"

TARGET_COLUMN_KEY="target_column"


## Model Trainer Realted variables

MODEL_TRAINER_ARTIFACT_DIR = "model_trainer"
MODEL_TRAINER_CONFIG_KEY = "model_trainer_config"
MODEL_TRAINER_TRAINED_MODEL_DIR_KEY = "trained_model_dir"
MODEL_TRAINER_TRAINED_MODEL_FILE_NAME_KEY = "model_file_name"
MODEL_TRAINER_BASE_ACCURACY_KEY = "base_accuracy"
MODEL_TRAINER_MODEL_CONFIG_DIR_KEY = "model_config_dir"
MODEL_TRAINER_MODEL_CONFIG_FILE_NAME_KEY = "model_config_file_name"


# Model Evaluation Related Variables

MODEL_EVALUATION_CONFIG_KEY = "model_evaluation_config"
MODEL_EVALUATION_FILE_NAME_KEY = "model_evaluation_file_name"
MODEL_EVALUATION_ARTIFACT_DIR = "model_evaluation"


# Model Pusher config key
MODEL_PUSHER_CONFIG_KEY = "model_pusher_config"
MODEL_PUSHER_MODEL_EXPORT_DIR_KEY = "model_export_dir"

BEST_MODEL_KEY = "best_model"
HISTORY_KEY = "history"
MODEL_PATH_KEY = "model_path"

EXPERIMENT_DIR_NAME="experiment"
EXPERIMENT_FILE_NAME="experiment.csv"











