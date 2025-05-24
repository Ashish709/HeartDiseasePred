import os,sys

import numpy as np
import pandas as pd
from sklearn.impute import KNNImputer
from sklearn.pipeline import Pipeline

from heartdisease.constants import TARGET_COLUMN,DATA_TRANSFORMATION_IMPUTER_PARAMS

from heartdisease.entity.artifact_entity import DataTransformationArtifact, DataValidationArtifact
from heartdisease.entity.config_entity import DataTransformationConfig

from heartdisease.exception.exception import CustomException
from heartdisease.logging.logger import logging

from heartdisease.utils.main_utils import save_numpy_array_data,save_object, read_data



class DataTransformation:
    def __init__(self,
                 data_validation_artifact: DataValidationArtifact,
                 data_transformation_config:DataTransformationConfig):
        try:
            self.data_validation_artifact = data_validation_artifact
            self.data_transformation_config = data_transformation_config
        except Exception as e:
            raise CustomException(e,sys)
        
        
        
    def get_data_transformer_object(cls)->Pipeline:
        """
        It initialises a KNNImputer object with the parameters specified in the training_pipeline.py file
        and returns a Pipeline object with the KNNImputer object as the first step.

        Args:
          cls: DataTransformation

        Returns:
          A Pipeline object
        """
        
        logging.info(
            "Entered get_data_trnasformer_object method of Trnasformation class"
        ) 
        
        try:
            imputer = KNNImputer(**DATA_TRANSFORMATION_IMPUTER_PARAMS)
            
            logging.info(
                f"Initiated KNN Imputer with {DATA_TRANSFORMATION_IMPUTER_PARAMS}"
            )
            
            processor = Pipeline([('imputer',imputer)])
            
            return processor
        
        except Exception as e:
            raise CustomException(e,sys)
        
    
    def initiate_data_transformation(self) -> DataTransformationArtifact:
        logging.info("Entered initiate_data_transformation method of DataTransformation class")
        try:
            logging.info("Starting data transformation")
            # print("valid_train_file_path",self.data_validation_artifact.valid_train_file_path)
            # print("valid_train_file_path",self.data_validation_artifact.valid_test_file_path)
            
            train_df = read_data(self.data_validation_artifact.valid_train_file_path)
            test_df = read_data(self.data_validation_artifact.valid_test_file_path)
            
            logging.info("Dependent and Target Variable Separation Started")
            ## training dataframe
            input_feature_train_df = train_df.drop(TARGET_COLUMN,axis=1)
            target_feature_train_df = train_df[TARGET_COLUMN]
            
            ## Test DataFrame
            input_feature_test_df = test_df.drop(TARGET_COLUMN,axis=1)
            target_feature_test_df = test_df[TARGET_COLUMN]
            logging.info("Dependent and Target Variable Separation Completed")
            
            
            #logging.info("")
            ## Getting Pre Precessor
            preprocessor = self.get_data_transformer_object()
            
            ## Creating Pre Precessor Object
            preprocessor_object = preprocessor.fit(input_feature_train_df)
            
            ## Transforming Train DF features
            transformed_input_train_feature = preprocessor_object.transform(input_feature_train_df)
            
            ## Transforming TEST DF features
            transformed_input_test_feature = preprocessor_object.transform(input_feature_test_df)
            
            
            # Creating Training & Testing Array
            train_arr = np.c_[transformed_input_train_feature, np.array(target_feature_train_df) ]
            test_arr = np.c_[ transformed_input_test_feature, np.array(target_feature_test_df) ]
            
            
            ## Saving Arrays & Object
            ## Train File
            save_numpy_array_data(self.data_transformation_config.transformed_train_file_path, train_arr)
            
            ## Test File
            save_numpy_array_data(self.data_transformation_config.transformed_test_file_path, test_arr)
            
            ## Save Preprocessor Object
            save_object(self.data_transformation_config.transformed_object_file_path, preprocessor_object)
            
            
            ## Artifacts
            data_transformation_artifacts = DataTransformationArtifact(
                transformed_object_file_path=self.data_transformation_config.transformed_object_file_path,
                transformed_train_file_path=self.data_transformation_config.transformed_train_file_path,
                transformed_test_file_path=self.data_transformation_config.transformed_test_file_path
            )
            
            return data_transformation_artifacts
            
            
            
            
            pass
        
        except Exception as e:
            raise CustomException(e,sys)
            

