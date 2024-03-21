import os, sys
from pathlib import Path

from waste_detection.logger import logging
from waste_detection.exception import CustomException

from waste_detection.config.config_manager import ConfigManager
from waste_detection.components.model_training import ModelTraining


try:
    config = ConfigManager()
    model_training = ModelTraining(config.get_model_training_config())
    model_training.train()

except Exception as e:
    raise CustomException(e, sys)


class ModelTrainingPipeline:
    def __init__(self):
        pass

    def main(sef):
        try:
            config = ConfigManager()
            model_training = ModelTraining(config.get_model_training_config())
            model_training.train()

        except Exception as e:
            raise CustomException(e, sys)
