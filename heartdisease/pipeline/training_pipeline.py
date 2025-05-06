import os
import sys

from heartdisease.exception.exception import CustomException
from heartdisease.logging.logger import logging

from heartdisease.entity.config_entity import (TrainingPipelineConfig, DataIngestionConfig)#, DataValidationConfig, DataTransformationConfig, ModelTrainerConfig)
from heartdisease.entity.artifact_entity import (DataIngestionArtifact)#, DataValidationArtifact, DataTransformationArtifact, ModelTrainerArtifact)   

from heartdisease.components.data_ingestion import DataIngestion


class TrainingPipeline:
    
    # Initiate TrainingPipelineCongfig
    def __init__(self):
        self.traing_pipeline_config = TrainingPipelineConfig
    
    
    def start_data_ingestion(self):
        try:
            self.data_ingestion_config = DataIngestionConfig(training_pipeline_config=self.traing_pipeline_config)
            
            data_ingestion = DataIngestion(data_ingestion_config=self.data_ingestion_config)    
            logging.info("")
            logging.info(f"{'>>'*20} Data Ingestion started {'<<'*20}")
            
            data_ingestion_artifact = data_ingestion.initiate_data_ingestion()
            
            logging.info("Data Ingestion completed and Artifact is created:", data_ingestion_artifact)
            logging.info(f"{'>>'*20} Data Ingestion completed and Artifact is created:  {data_ingestion_artifact} {'<<'*20}")
            
            return data_ingestion_artifact
        
        except Exception as e:
            raise CustomException(e, sys)

  