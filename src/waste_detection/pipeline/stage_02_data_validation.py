import os,sys
from pathlib import Path

from waste_detection.logger import logging
from waste_detection.exception import CustomException

from waste_detection.config.config_manager import ConfigManager
from waste_detection.components.data_validation import DataValidation


class DataValidationTrainingPipeline:
    def __init__(self):
        pass

    def main(sef):
        try:
            config = ConfigManager()
            data_validation = DataValidation(config.get_data_validation_config())
            data_validation.update_path()

        except Exception as e:
            raise CustomException(e,sys)

    



