import os
from dataclasses import dataclass
from datetime import datetime
from PlasticBottleDetection.constant.PipelineConfig import *


@dataclass
class PipelineConfig:
    artifacts_dir: str = ARTIFACTS_DIR


Pipeline_Config: PipelineConfig = PipelineConfig()


@dataclass
class DataIngestionConfig:
    data_ingestion_dir: str = os.path.join(
        Pipeline_Config.artifacts_dir, DATA_INGESTION_DIR_NAME
    )

    unzipped_data_file_path: str = os.path.join(
        data_ingestion_dir, DATA_INGESTION_UNZIPPED_DATA_DIR
    )

    data_download_url: str = DATA_DOWNLOAD_URL


@dataclass
class DataValidationConfig:
    data_validation_dir: str = os.path.join(
        Pipeline_Config.artifacts_dir, DATA_VALIDATION_DIR_NAME
    )

    valid_status_file_dir: str = os.path.join(
        data_validation_dir, DATA_VALIDATION_STATUS_FILE
    )

    required_file_list = DATA_VALIDATION_ALL_REQUIRED_FILES


@dataclass
class ModelTrainerConfig:
    model_trainer_dir: str = os.path.join(
        Pipeline_Config.artifacts_dir, MODEL_TRAINER_DIR_NAME
    )

    weight_name = MODEL_TRAINER_PRETRAINED_WEIGHT_NAME

    no_epochs = MODEL_TRAINER_NO_EPOCHS

    batch_size = MODEL_TRAINER_BATCH_SIZE
