from heartdisease.logging.logger import logging
from heartdisease.exception.exception import CustomException

import os, sys, yaml, dill, pickle

import numpy as np
import pandas as pd
from sklearn.model_selection import GridSearchCV 
from sklearn.metrics import r2_score 


def read_yaml_file(file_path:str)-> dict:
    try:
        with open(file_path, 'rb') as yaml_file:
            return yaml.safe_load(yaml_file)
    
    except Exception as e:
        raise CustomException(e,sys)


def write_yaml_file(file_path:str, content:object, replace:bool=False) -> None:
    try:
        if replace:
            if os.path.exists(file_path):
                os.remove(file_path)
                
        os.makedirs(os.path.dirname(file_path),exist_ok=True)
        
        with open(file_path, "w") as file:
            yaml.dump(content, file)
        
    
    except Exception as e:
        raise CustomException(e,sys)
    
    
def read_data(file_path:str) -> pd.DataFrame:
    try:
        return pd.read_csv(file_path)
        
    except Exception as e:
        raise CustomException(e,sys)
    
