import os
import sys

import pandas as pd

from heartdisease.exception.exception import CustomException
from heartdisease.logging.logger import logging

from heartdisease.entity.config_entity import DataIngestionConfig,DataValidationConfig
from heartdisease.entity.artifact_entity import DataValidationArtifact, DataIngestionArtifact
from heartdisease.constants import SCHEMA_FILE_PATH

from heartdisease.utils.main_utils import read_yaml_file, write_yaml_file, read_data

from scipy.stats import ks_2samp



class DataValidation:
    def __init__(self, 
                 data_ingestion_artifact: DataIngestionArtifact,
                 data_validation_config: DataValidationConfig                 ):
        try:
            self.data_ingestion_artifact = data_ingestion_artifact
            self.data_validation_config = data_validation_config
            self.schema_config = read_yaml_file(SCHEMA_FILE_PATH)
        
        except Exception as e:
            raise CustomException(e,sys)
        
    
    def validate_number_of_columns(self, dataframe:pd.DataFrame)->bool:
        try:
            numbner_of_columns = len(self.schema_config['columns'])
            logging.info(f"Required Number of Columns {numbner_of_columns}")
            logging.info(f"Data Frame has colums: {len(dataframe.columns)}")
            
            if len(dataframe.columns) == numbner_of_columns:
                    return True
            
            return False
    
        except Exception as e:
            raise CustomException(e,sys)
        
        
    
    def detect_dataset_drift(self,base_df,current_df,threshold=0.05) -> bool:
        try:
            status = True
            report = {}
            
            for column in base_df.columns:
                d1 = base_df[column]
                d2 = current_df[column]
                
                is_same_dist = ks_2samp(d1,d2)
                
                if threshold <= is_same_dist.pvalue:
                    is_found=False
                else:
                    is_found= True
                    status = False
                    
                report.update({
                    column: {
                        "p_value" : float(is_same_dist.pvalue),
                        "drift_status":is_found
                    }
                })
            
            drift_report_file_path = self.data_validation_config.drift_report_file_path
            drift_report_file_name = self.data_validation_config.data_drift_file_name
            
            # Create Directory
            os.makedirs(drift_report_file_path,exist_ok=True)
            file_path = os.path.join(drift_report_file_path,drift_report_file_name)
            dir_path = os.path.dirname(file_path)
            
            os.makedirs(dir_path,exist_ok=True)
            
            write_yaml_file(file_path=file_path,content=report)
        
        except Exception as e:
            raise CustomException(e,sys)
        
        
        
    
    def initiate_data_validation(self) -> DataValidationArtifact:
        try:
            train_file_path = self.data_ingestion_artifact.train_file_path
            test_file_path = self.data_ingestion_artifact.test_file_path
            
            ## Read the data from Train & Test
            train_dataframe = read_data(train_file_path)
            test_dataframe = read_data(test_file_path)
            
            
            ## Validate Number of Columns
            status = self.validate_number_of_columns(dataframe=train_dataframe)
            if not status:
                error_message = f"Train DataFrame does not contain all Columns.\n"
                
            status = self.validate_number_of_columns(dataframe=test_dataframe)
            if not status:
                error_message = f"Test DataFrame does not contain all Columns.\n"
                
            
            ## Lets Check Data Drift
            status = self.detect_dataset_drift(base_df=train_dataframe,current_df=test_dataframe)
            dir_path = os.path.dirname(self.data_validation_config.valid_train_file_path)
            os.makedirs(dir_path,exist_ok=True)
            
            train_dataframe.to_csv(
                self.data_validation_config.valid_train_file_path, index=True, header =True
            )
            
            test_dataframe.to_csv(
                self.data_validation_config.valid_test_file_path, index=True, header =True
            )
            
            
            ## Output Store is Artifacts
            data_validation_artifact = DataValidationArtifact(
                validation_status=status,
                valid_train_file_path=self.data_validation_config.valid_train_file_path,
                valid_test_file_path=self.data_validation_config.valid_test_file_path,
                invalid_train_file_path=self.data_validation_config.invalid_train_file_path,
                invalid_test_file_path=self.data_validation_config.invalid_test_file_path,
                drift_report_file_path=self.data_validation_config.drift_report_file_path
            )
            
            return data_validation_artifact
        
        except Exception as e:
            raise CustomException(e,sys)
        
        
        
    

