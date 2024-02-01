import os,sys
from pathlib import Path

from waste_detection.logger import logging
from waste_detection.exception import CustomException

from waste_detection.config.config_manager import ConfigManager
from waste_detection.components.data_ingestion import DataIngestion


class DataIngestionTrainingPipeline:
    def __init__(self):
        pass

    def main(sef):
        try:
            config = ConfigManager()
            data_ingestion = DataIngestion(config.get_data_ingestion_config())
            # data_ingestion.download_data_from_github()
            data_ingestion.download_data_from_drive()
            data_ingestion.extract_zip_file()

        except Exception as e:
            raise CustomException(e, sys)




