import os, sys
from pathlib import Path

from waste_detection.logger import logging
from waste_detection.exception import CustomException

from waste_detection.utils.common import read_yaml, create_directories
from waste_detection.constants import *

from waste_detection.entity.config_entity import DataIngestionConfig
from waste_detection.entity.config_entity import DataValidationConfig
from waste_detection.entity.config_entity import ModelTrainingConfig


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

    def get_data_validation_config(self) -> DataValidationConfig:
        config = self.config.data_validation

        # create_directories([config.root_dir])

        data_validation_config = DataValidationConfig(
            # root_dir = config.root_dir,
            # status = config.status,
            data_yaml=config.data_yaml,
            train_path=config.train_path,
            valid_path=config.valid_path,
        )

        return data_validation_config

    def get_model_training_config(self) -> ModelTrainingConfig:
        config = self.config.model_training
        params = self.params.train

        create_directories([config.root_dir])
        create_directories([config.history])

        model_training_config = ModelTrainingConfig(
            root_dir=Path(config.root_dir),
            yolov5_root=Path(config.yolov5_root),
            yolov5_models=Path(config.yolov5_models),
            custom_yolov5=Path(config.custom_yolov5),
            train_path=Path(config.train_path),
            yolov5_runs=Path(config.yolov5_runs),
            history=Path(config.history),
            git_URL=config.git_URL,
            IMAGE_SIZE=params.IMAGE_SIZE,
            BATCH_SIZE=params.BATCH_SIZE,
            EPOCHS=params.EPOCHS,
            DATA=Path(params.DATA),
            WEIGHTS=params.WEIGHTS,
            NAME=params.NAME,
        )

        return model_training_config
