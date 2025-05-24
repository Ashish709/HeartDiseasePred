import sys
from heartdisease.logging.logger import logging
from heartdisease.exception.exception import CustomException


from heartdisease.pipeline.training_pipeline import TrainingPipeline
from heartdisease.entity.config_entity import TrainingPipelineConfig, DataIngestionConfig,DataValidationConfig,DataTransformationConfig, ModelTrainerConfig
from heartdisease.entity.artifact_entity import DataIngestionArtifact,DataValidationArtifact,DataTransformationArtifact, ModelTrainerArtifact
from heartdisease.components.data_ingestion import DataIngestion
from heartdisease.components.data_validation import DataValidation
from heartdisease.components.data_transformation import DataTransformation
from heartdisease.components.model_trainer import ModelTrainer

# ###### DATA INGESTION
# if __name__=='__main__':
#     try:
#         training_pipeline = TrainingPipelineConfig()
        
#         data_ingestion_config = DataIngestionConfig(training_pipeline_config=TrainingPipelineConfig())
#         data_ingestion = DataIngestion(data_ingestion_config=data_ingestion_config)
        
#         logging.info("Initiated the Data Ingestion")
        
#         data_ingestion_artifact = data_ingestion.initiate_data_ingestion()
#         print(data_ingestion_artifact)
#         logging.info(f"Data Ingestion completed and Artifact is created:  {data_ingestion_artifact}")
        
#     except Exception as e:
#         logging.error("Exception occured in the main method")
#         raise CustomException(e,sys)
    


# ### DATA VALIDATION    
# if __name__ == "__main__":
#     try:
#         trainingpipelineconfig = TrainingPipelineConfig()
#         dataingestionconfg = DataIngestionConfig(trainingpipelineconfig)
#         dataingestion = DataIngestion(dataingestionconfg)
        
#         logging.info("Initiate the Data Ingestion")
        
#         dataingestionartifact = dataingestion.initiate_data_ingestion()
#         logging.info("Data Ingestion Completed")
#         print(dataingestionartifact)
        
#         data_validation_config = DataValidationConfig(trainingpipelineconfig)
#         data_validation = DataValidation(dataingestionartifact, data_validation_config)
        
#         logging.info("Initiate the Data Validation")
#         data_validation_artifact = data_validation.initiate_data_validation()
#         logging.info("Data Validation Completed")
#         print(data_validation_artifact)
    
#     except Exception as e:
#         raise CustomException(e,sys)
    

# ### DATA TRANSFORMATION    
# if __name__ == "__main__":
#     try:
#         trainingpipelineconfig = TrainingPipelineConfig()
#         dataingestionconfg = DataIngestionConfig(trainingpipelineconfig)
#         dataingestion = DataIngestion(dataingestionconfg)
        
#         logging.info("Initiate the Data Ingestion")
        
#         dataingestionartifact = dataingestion.initiate_data_ingestion()
#         logging.info("Data Ingestion Completed")
#         print(dataingestionartifact)
        
#         data_validation_config = DataValidationConfig(trainingpipelineconfig)
#         data_validation = DataValidation(dataingestionartifact, data_validation_config)
        
#         logging.info("Initiate the Data Validation")
#         data_validation_artifact = data_validation.initiate_data_validation()
#         logging.info("Data Validation Completed")
#         print(data_validation_artifact)
        
        
#         data_transformation_config = DataTransformationConfig(trainingpipelineconfig)
#         logging.info("Initiate the Data Transformation")
#         data_transformation = DataTransformation(data_validation_artifact,data_transformation_config)
#         data_transformation_artifact = data_transformation.initiate_data_transformation()
#         logging.info("Data Transformation Completed")
#         print("data_transformation_artifact:",data_transformation_artifact)
    
#     except Exception as e:
#         raise CustomException(e,sys)



### MODEL TRAINER    
if __name__ == "__main__":
    try:
        trainingpipelineconfig = TrainingPipelineConfig()
        dataingestionconfg = DataIngestionConfig(trainingpipelineconfig)
        dataingestion = DataIngestion(dataingestionconfg)
        
        logging.info("Initiate the Data Ingestion")
        
        dataingestionartifact = dataingestion.initiate_data_ingestion()
        logging.info("Data Ingestion Completed")
        print(dataingestionartifact)
        
        data_validation_config = DataValidationConfig(trainingpipelineconfig)
        data_validation = DataValidation(dataingestionartifact, data_validation_config)
        
        logging.info("Initiate the Data Validation")
        data_validation_artifact = data_validation.initiate_data_validation()
        logging.info("Data Validation Completed")
        print(data_validation_artifact)
        
        
        data_transformation_config = DataTransformationConfig(trainingpipelineconfig)
        logging.info("Initiate the Data Transformation")
        data_transformation = DataTransformation(data_validation_artifact,data_transformation_config)
        data_transformation_artifact = data_transformation.initiate_data_transformation()
        logging.info("Data Transformation Completed")
        print("data_transformation_artifact:",data_transformation_artifact)
        
        logging.info("Models Test Training Started")
        model_trainder_config = ModelTrainerConfig(trainingpipelineconfig)
        model_trainer = ModelTrainer(model_trainder_config, data_transformation_artifact)
        model_trainer_artifact = model_trainer.initiated_model_trainer()
        logging.info("Models Test Training Completed")
    
    except Exception as e:
        raise CustomException(e,sys)        


# import mlflow

# mlflow.set_tracking_uri("your_tracking_uri")
# logging.getLogger().setLevel(logging.INFO)  # Reset logging level
# logging.getLogger("mlflow").setLevel(logging.WARNING)  # Suppress MLflow logs if needed
    
    
    
    





