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
