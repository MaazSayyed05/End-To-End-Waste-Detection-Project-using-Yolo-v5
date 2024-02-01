
import os,sys
from pathlib import Path

from waste_detection.logger import logging
from waste_detection.exception import CustomException

from waste_detection.utils.common import read_yaml, create_directories
from waste_detection.constants import *

from waste_detection.entity.config_entity import DataIngestionConfig


class ConfigManager:
    def __init__(
        self, config_file_path=CONFIG_FILE_PATH, params_file_path=PARAMS_FILE_PATH
    ):
        self.config = read_yaml(config_file_path)
        self.params = read_yaml(params_file_path)

        create_directories([self.config.artifacts_root])

    def get_data_ingestion_config(self) -> DataIngestionConfig:
        config = self.config.data_ingestion

        create_directories([config.root_dir])
        data_ingestion_config = DataIngestionConfig(
            root_dir=config.root_dir,
            feature_path=config.feature_path,
            data_URL=config.data_URL,
            data_path=config.data_path,
        )

        return data_ingestion_config
