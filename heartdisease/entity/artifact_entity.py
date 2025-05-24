from dataclasses import dataclass

# This is for the outputs of the components

@dataclass
class DataIngestionArtifact:
    train_file_path:str
    test_file_path:str
    


@dataclass
class DataValidationArtifact:
    validation_status:bool
    valid_train_file_path:str
    valid_test_file_path:str
    invalid_train_file_path:str
    invalid_test_file_path:str
    drift_report_filee_path:str