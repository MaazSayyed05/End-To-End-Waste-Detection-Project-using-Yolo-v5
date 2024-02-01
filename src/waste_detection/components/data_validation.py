import os, sys
from pathlib import Path

from waste_detection.logger import logging
from waste_detection.exception import CustomException

from waste_detection.utils.common import read_yaml, update_yaml_file

from waste_detection.entity.config_entity import DataValidationConfig


class DataValidation:
    def __init__(self, config: DataValidationConfig):
        self.config = config

    def update_path(self):
        # Read data.yaml
        # Change train, test, valid path
        try:

            data = read_yaml(Path(self.config.data_yaml))

            update_yaml_file(self.config.data_yaml, "train", self.config.train_path)
            update_yaml_file(self.config.data_yaml, "val", self.config.valid_path)
            # update_yaml_file(self.config.data_yaml, "test", self.config.test_path)

        except Exception as e:
            # logging.error(e)
            raise CustomException(e,sys)