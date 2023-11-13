import os
import sys
import zipfile
import gdown
from PlasticBottleDetection.logger import logging
from PlasticBottleDetection.exception import AppException
from PlasticBottleDetection.entity.config_entity import DataIngestionConfig
from PlasticBottleDetection.entity.artifacts_entity import DataIngestionArtifact


class DataIngestion:
    def __init__(
        self, data_ingestion_config: DataIngestionConfig = DataIngestionConfig()
    ):
        try:
            self.data_ingestion_config = data_ingestion_config
        except Exception as e:
            raise AppException(e, sys)

    def download_data(self) -> str:
        """
        Fetch data from the url
        """

        try:
            dataset_url = self.data_ingestion_config.data_download_url
            zip_download_dir = self.data_ingestion_config.data_ingestion_dir
            os.makedirs(zip_download_dir, exist_ok=True)
            data_file_name = "data.zip"
            zip_file_path = os.path.join(zip_download_dir, data_file_name)
            logging.info(
                f"Downloading data from {dataset_url} into file {zip_file_path}"
            )

            file_id = dataset_url.split("/")[-2]
            prefix = "https://drive.google.com/uc?/export=download&id="
            gdown.download(prefix + file_id, zip_file_path)

            logging.info(
                f"Downloaded data from {dataset_url} into file {zip_file_path}"
            )

            return zip_file_path

        except Exception as e:
            raise AppException(e, sys)

    def extract_zip_file(self, zip_file_path: str) -> str:
        """
        zip_file_path: str
        Extracts the zip file into the data directory
        Function returns None
        """
        try:
            unzipped_data_path = self.data_ingestion_config.unzipped_data_file_path
            os.makedirs(unzipped_data_path, exist_ok=True)
            with zipfile.ZipFile(zip_file_path, "r") as zip_ref:
                zip_ref.extractall(unzipped_data_path)
            logging.info(
                f"Extracting zip file: {zip_file_path} into dir: {unzipped_data_path}"
            )

            return unzipped_data_path

        except Exception as e:
            raise AppException(e, sys)

    def initiate_data_ingestion(self) -> DataIngestionArtifact:
        logging.info("Entered initiate_data_ingestion method of Data_Ingestion class")
        try:
            zip_file_path = self.download_data()
            unzipped_data_path = self.extract_zip_file(zip_file_path)

            data_ingestion_artifact = DataIngestionArtifact(
                data_zip_file_path=zip_file_path, unzipped_data_path=unzipped_data_path
            )

            logging.info(
                "Exited initiate_data_ingestion method of Data_Ingestion class"
            )
            logging.info(f"Data ingestion artifact: {data_ingestion_artifact}")

            return data_ingestion_artifact

        except Exception as e:
            raise AppException(e, sys)
