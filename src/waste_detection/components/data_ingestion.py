import os
import sys
import zipfile
import gdown
from pathlib import Path

from waste_detection.logger import logging
from waste_detection.exception import CustomException

from waste_detection.entity.config_entity import DataIngestionConfig



class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config

    def download_data_from_github(self):
        if not os.path.exists(self.config.data_file):
            filename, headers = request.urlretrieve(
                url=self.config.data_url, filename=self.config.data_file
            )

            logger.info(f"{filename} download! with following info: \n {headers}")

        else:
            logger.info(f"File already exists.")

    def download_data_from_drive(self):
        """
        Fetch data from the url
        """

        try:
            if not os.path.exists(self.config.data_path):
                dataset_url = self.config.data_URL
                zip_download_dir = self.config.root_dir
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
            
            else:
                logging.info(f"File already exists.")

        except Exception as e:
            raise CustomException(e, sys)

    def extract_zip_file(self):
        """
        zip_file_pah: str
        Extarcts the zip file into the  data directory
        Function return None
        """
        unzip_path = self.config.feature_path
        os.makedirs(unzip_path, exist_ok=True)
        # logger.info(f"{self.config.local_data_file}")
        with zipfile.ZipFile(self.config.data_path, "r") as zip_ref:
            zip_ref.extractall(unzip_path)

        logging.info(f"{self.config.data_path} unzipped to {unzip_path}")
