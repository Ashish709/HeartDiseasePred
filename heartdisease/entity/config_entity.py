from datetime import datetime
import os
from heartdisease import constants

# It is for configuration purpose and it is input for every components

class TrainingPipelineConfig:
    def __init__(self):
        timestamp = constants.CURRENT_TIME_STAMP
        self.pipelinename = constants.PIPELINE_NAME
        self.artifact_name = constants.ARTIFACT_DIR_NAME
        self.artifact_dir = os.path.join(self.artifact_name,timestamp)
        self.model_dir = constants.SAVED_MODEL_DIR
        self.timestamp:str = timestamp
        
    
class DataIngestionConfig:
    def __init__(self,training_pipeline_config:TrainingPipelineConfig):
        
        
        ## File Path
        self.file_path:str = constants.FILE_PATH
        
        ## RAW Directory
        self.data_ingestion_dir:str = os.path.join(
            training_pipeline_config.artifact_name, 
            constants.DATA_INGESTION_ARTIFACT_DIR
        ) 
        
        # RAW data data File Path
        self.feature_store_file_path:str = os.path.join(
            self.data_ingestion_dir, 
            constants.DATA_INGESTION_RAW_DATA_DIR_KEY, constants.FILE_NAME
        )
        
        
        ## Training File Path
        self.training_file_path:str = os.path.join(
            self.data_ingestion_dir, 
            #
            constants.TRAIN_FILE_NAME
        )
        
        
        ## Test File Path
        self.test_file_path:str = os.path.join(
            self.data_ingestion_dir,
            #constants.DATA_INGESTION_INGESTED_DIR_NAME_KEY,
            constants.TEST_FILE_NAME
        )
        
        ## Train Test Split Ratio
        self.train_test_split_ratio:float = constants.DATA_INGESTION_TRAIN_TEST_SPLIT_RATIO
        
        