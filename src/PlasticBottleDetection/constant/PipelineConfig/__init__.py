ARTIFACTS_DIR: str = "artifacts"

"""
Data Ingestion format
"""
DATA_INGESTION_DIR_NAME: str = "data_ingestion"

DATA_INGESTION_UNZIPPED_DATA_DIR: str = "unzipped_data"

DATA_DOWNLOAD_URL: str = (
    "https://drive.google.com/file/d/1riMsmekU_jhuJoAOv_dP7o3EXsXZ6rbr/view?usp=sharing"
)


"""
Data Validation format
"""

DATA_VALIDATION_DIR_NAME: str = "data_validation"

DATA_VALIDATION_STATUS_FILE = "status.txt"

DATA_VALIDATION_ALL_REQUIRED_FILES = ["train", "valid", "test", "data.yaml"]


"""
MODEL TRAINER format
"""
MODEL_TRAINER_DIR_NAME: str = "model_trainer"

MODEL_TRAINER_PRETRAINED_WEIGHT_NAME: str = "yolov5s.pt"

MODEL_TRAINER_NO_EPOCHS: int = 1

MODEL_TRAINER_BATCH_SIZE: int = 16
