import os
from src.constants import *
from dataclasses import dataclass
from datetime import datetime

TIMESTAMP: str = datetime.now().strftime("%m_%d_%Y_%H_%M_%S") # use to keep output organized by time/version

@dataclass
class TrainingPipelineConfig:
    pipeline_name: str = PIPELINE_NAME # pipeline name
    artifact_dir: str = os.path.join(ARTIFACT_DIR, TIMESTAMP) # all artifacts are saved here
    timestamp: str = TIMESTAMP # store same timestamp use in artifact_dir

training_pipeline_config: TrainingPipelineConfig = TrainingPipelineConfig() # instance of TrainingPipelineConfig

@dataclass
class DataIngestionConfig:
    data_ingestion_dir:str = os.path.join(training_pipeline_config.artifact_dir,
                                      DATA_INGESTION_DIR_NAME) # base dir to store all the data-ingestion related files
    feature_store_file_path: str = os.path.join(data_ingestion_dir, 
                                                DATA_INGESTION_FEATURE_STORE_DIR, FILE_NAME) # path to full dataset
    training_file_path: str = os.path.join(data_ingestion_dir, 
                                           DATA_INGESTION_INGESTED_DIR, TRAIN_FILE_NAME) # path to save train data
    testing_file_path: str = os.path.join(data_ingestion_dir, 
                                           DATA_INGESTION_INGESTED_DIR, TEST_FILE_NAME) # path to save test data
    train_test_split_ratio: float = DATA_INGESTION_TRAIN_TEST_SPLIT_RATIO
    collection_name: str = DATA_INGESTION_COLLECTION_NAME

@dataclass
class DataValidationConfig:
    data_validation_dir: str = os.path.join(training_pipeline_config.artifact_dir, DATA_VALIDATION_DIR_NAME)
    validation_report_file_path: str = os.path.join(data_validation_dir, DATA_VALIDATION_REPORT_FILE_NAME)






