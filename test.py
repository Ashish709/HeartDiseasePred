import sys
from heartdisease.logging.logger import logging
from heartdisease.exception.exception import CustomException


from heartdisease.pipeline.training_pipeline import TrainingPipeline
from heartdisease.entity.config_entity import TrainingPipelineConfig, DataIngestionConfig
from heartdisease.entity.artifact_entity import DataIngestionArtifact
from heartdisease.components.data_ingestion import DataIngestion

if __name__=='__main__':
    try:
        training_pipeline = TrainingPipelineConfig()
        
        data_ingestion_config = DataIngestionConfig(training_pipeline_config=TrainingPipelineConfig())
        data_ingestion = DataIngestion(data_ingestion_config=data_ingestion_config)
        
        logging.info("Initiated the Data Ingestion")
        
        data_ingestion_artifact = data_ingestion.initiate_data_ingestion()
        print(data_ingestion_artifact)
        logging.info(f"Data Ingestion completed and Artifact is created:  {data_ingestion_artifact}")
        
    except Exception as e:
        logging.error("Exception occured in the main method")
        raise CustomException(e,sys)
    
    
    
    
    
    
    
    
    





