from datetime import datetime
import os
from heartdisease import constants

# It is for configuration purpose and it is input for every components

class TrainingPipelineConfig:
    def __init__(self):
        timestamp = constants.CURRENT_TIME_STAMP
        self.pipelinename = constants.PIPELINE_NAME
        self.artifact_dir = constants.ARTIFACT_DIR_NAME
        self.artifact_name = os.path.join(self.artifact_dir,timestamp)
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
        



class DataValidationConfig:
    def __init__(self,training_pipeline_config:TrainingPipelineConfig):
        
        
        ## Data Validation Dir
        self.data_validation_dir = os.path.join(
            training_pipeline_config.artifact_name,
            constants.DATA_VALIDATION_DIR_NAME
        )
        
        ## Valid Data Dir
        self.valid_data_dir = os.path.join(
            self.data_validation_dir,
            constants.DATA_VALIDATION_VALID_DIR
        )
        
        ## Invalid Data Dir
        self.invalid_data_dir = os.path.join(
            self.data_validation_dir,
            constants.DATA_VALIDATION_INVALID_DIR  
        )     
        
        
        ## valid train file path
        self.valid_train_file_path = os.path.join(
            self.valid_data_dir,
            constants.TRAIN_FILE_NAME
        )
        
        ## validt test file path
        self.valid_test_file_path = os.path.join(
            self.valid_data_dir,
            constants.TEST_FILE_NAME
        )
        
        
        ## invalid train file path
        self.invalid_train_file_path  = os.path.join(
            self.invalid_data_dir,
            constants.TRAIN_FILE_NAME
        )
        
        ## invalid test file path
        self.invalid_test_file_path = os.path.join(
            self.invalid_data_dir,
            constants.TEST_FILE_NAME
        )
        
        
        ## Drift Report Path
        self.drift_report_file_path = os.path.join(
            self.data_validation_dir,
            constants.DATA_VALIDATION_DRIFT_REPORT_DIR
        )
        
        ## Dirft Report Name
        self.data_drift_file_name = os.path.join(
            self.drift_report_file_path,
            constants.DATA_VALIDATION_DRIFT_REPORT_FILE_NAME
        )
       
       

class DataTransformationConfig:
    def __init__(self, training_pipeline_config:TrainingPipelineConfig):
        
        ## Data Transformation Dir
        self.data_transformation_dir = os.path.join(
            training_pipeline_config.artifact_name,
            constants.DATA_TRANSFORMATION_DIR_NAME
        )
        
        ## Transformed Train File Path
        self.transformed_train_file_path:str = os.path.join(
            self.data_transformation_dir,
            constants.DATA_TRANSFORMATION_TRANSFORMED_DATA_DIR,
            constants.DATA_TRANSFORMATION_TRAIN_FILE_PATH.replace('csv','npy')
        )
        
        ## Transformed Test File Path
        self.transformed_test_file_path:str = os.path.join(
            self.data_transformation_dir,
            constants.DATA_TRANSFORMATION_TRANSFORMED_DATA_DIR,
            constants.DATA_TRANSFORMATION_TEST_FILE_PATH.replace('csv','npy')
        )
        
        ## Transformed object file path
        self.transformed_object_file_path:str = os.path.join(
            self.data_transformation_dir,
            constants.DATA_TRANSFORMATION_TRANSFORMED_OBJECT_DIR,
            constants.PREPROCESSING_OBJECT_FILE_NAME
        )
        


class ModelTrainerConfig:
    def __init__(self, training_pipeline_config:TrainingPipelineConfig):
        
        self.model_trainer_dir:str = os.path.join(
            training_pipeline_config.artifact_name,
            constants.MODEL_TRAINER_DIR_NAME 
        )
        
        self.trained_model_file_path = os.path.join(
            self.model_trainer_dir,
            constants.MODEL_FILE_NAME
        )
        
        self.expected_accuracy:float = constants.MODEL_TRAINER_EXPECTED_SCORE
        self.overfitting_underfitting_threshold = constants.MODEL_TRAINER_OVER_FIITING_UNDER_FITTING_THRESHOLD
        
        
        
        