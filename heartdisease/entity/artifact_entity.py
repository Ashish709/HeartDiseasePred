from dataclasses import dataclass

# This is for the outputs of the components

@dataclass
class DataIngestionArtifact:
    train_file_path:str
    test_file_path:str
    
