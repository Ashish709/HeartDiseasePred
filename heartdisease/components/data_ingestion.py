import os
import sys
import pymongo
from typing import List
from sklearn.model_selection import train_test_split
import pandas as pd
import numpy as np

from heartdisease.exception.exception import CustomException
from heartdisease.logging.logger import logging


from heartdisease.entity.config_entity import DataIngestionConfig
from heartdisease.entity.artifact_entity import DataIngestionArtifact



class DataIngestion:
    
    # initiated DataIngestionConfig
    def __init__(self,data_ingestion_config:DataIngestionConfig):
        try:
            self.data_ingestion_config = data_ingestion_config
        
        except Exception as e:
            raise CustomException(e,sys)
        
    
    ## Read the data from our sorce and then store it on our Artifact dir
    
    def read_local_database(self):
        """
        Read Data from Source and store it in Artifact Dir
        """
        
        try:
            logging.info(f"{'>>'*20} Reading Data From Loacl Directory {'<<'*20}")
            data_frame = pd.read_csv("data/heart.csv")
            
            return data_frame
            
        
        except Exception as e:
            raise CustomException(e,sys)
    
    # Already have data in RAW format in local folder no need to store raw data again,
    ## Still code for this is as below
    # def export_data_raw_feature_store(self,dataframe:pd.DataFrame):
    #     try:
    #         feature_store_file_path = self.data_ingestion_config.feature_store_file_path
        
    #     ## Create Folder to store RAW Data
    #         dir_path = os.path.dirname(feature_store_file_path)
    #         os.makedirs(dir_path,exist_ok=True)
            
    #         dataframe.to_csv(feature_store_file_path,index=False,header=True)
            
    #         return dataframe
        
        except Exception as  e:
            raise CustomException(e,sys)
        
    
    
    ## Split Data into Train & Test
    def split_data_as_train_test(self, dataframe:pd.DataFrame):
        try:
            ## Split the data into Train and Test
            ## Train Test Split Ratio is 0.2 i.e 80% data for training and 20% data for testing
            logging.info(f"{'>>'*20} Performing Train Test Split on the DataFrame {'<<'*20}")
            train_set, test_set = train_test_split(dataframe, 
                                                   test_size=self.data_ingestion_config.train_test_split_ratio, 
                                                   random_state=42)
            
            logging.info(f"{'>>'*20}  Train Test Split on the DataFrame is completed {'<<'*20}")
            
            
            ## Creating Ingested data Directory
            ingested_dir = os.path.dirname(self.data_ingestion_config.training_file_path)
            os.makedirs(ingested_dir,exist_ok=True)
            
            
            ## Saving the Train and Test data into CSV file
            logging.info(f"{'>>'*20} Exporting Data into Train & Test file Paths Started. {'<<'*20}")
            
            train_set.to_csv(self.data_ingestion_config.training_file_path, index=False, header=True)
            test_set.to_csv(self.data_ingestion_config.test_file_path, index=False, header=True)

            logging.info(f"{'>>'*20} Exporting Data into Train & Test file Paths Completed. {'<<'*20}")
            
        
        except Exception as e:
            raise CustomException(e,sys)
        
    
    def initiate_data_ingestion(self)-> DataIngestionArtifact:

        try:
            #logging.info("Exporting Data into Feature Store")
            
            dataframe = self.read_local_database()
            
            ## Exporting Data into Feature Store
            # dataframe = self.export_data_raw_feature_store(dataframe)
            
            # logging.info("Splitting the data into Train and Test")
            
            ## Splitting the data into Train and Test
            self.split_data_as_train_test(dataframe=dataframe)
            
            # logging.info("Data Ingestion is completed")
            
            data_ingestion_artifact = DataIngestionArtifact(
                train_file_path=self.data_ingestion_config.training_file_path,
                test_file_path=self.data_ingestion_config.test_file_path
            )
            
            return data_ingestion_artifact
        
            
        
        except Exception as e:
            raise CustomException(e,sys)    



