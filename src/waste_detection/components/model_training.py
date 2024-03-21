import os, sys
from pathlib import Path
from waste_detection.utils.common import read_yaml, read_modify_write_yaml

import torch

from waste_detection.logger import logging
from waste_detection.exception import CustomException

import subprocess

import yaml

from datetime import datetime


from waste_detection.entity.config_entity import ModelTrainingConfig


class ModelTraining:
    def __init__(self, config: ModelTrainingConfig):
        self.config = config

    def train(self):
        try:
            # Specify the URL of the GitHub repository
            # repo_url = "https://github.com/username/repo.git"

            # Specify the directory where you want to clone the repository
            root = os.getcwd()
            clone_dir = os.path.join(root, self.config.yolov5_root)

            # Create the command to clone the repository
            # command = f"git clone {self.config.git_URL}"

            # Execute the command using os.system()
            # os.system(command)

            ## 2. Change data.yml file and save custom data.yml file in
            yolov5_pt = self.config.WEIGHTS.split(".")[0] + ".yaml"
            yolov5_pt_path = os.path.join(self.config.yolov5_models, yolov5_pt)
            print(yolov5_pt, yolov5_pt_path)

            data = read_yaml(Path(self.config.DATA))
            data_pt = read_yaml(Path(yolov5_pt_path))

            data_pt.nc = data.nc

            with open(self.config.custom_yolov5, "w") as f:
                yaml.dump(data_pt, f)

            print(data_pt, data_pt.nc)
            read_modify_write_yaml(
                yolov5_pt_path, self.config.custom_yolov5, {"nc": data.nc}
            )

            ## 3. Train the model
            # os.system(f'python {self.config.train_path} --img {self.config.IMAGE_SIZE} --batch {self.config.BATCH_SIZE} --epochs {self.config.EPOCHS} --data {os.path.abspath(self.config.DATA)} --weights {self.config.WEIGHTS} --name {self.config.NAME} --cache')

            command = f"python {self.config.train_path} --img {self.config.IMAGE_SIZE} --batch {self.config.BATCH_SIZE} --epochs {self.config.EPOCHS} --data {os.path.abspath(self.config.DATA)} --weights {self.config.WEIGHTS} --name {self.config.NAME} --cache"
            result = subprocess.run(
                command,
                shell=True,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
            )
            print(result)

            crt_time = "runs_" + datetime.now().strftime("%d_%m_%Y_%H_%M_%S") + "/"
            runs_path = os.path.join(self.config.history, crt_time)

            yolov5_runs = os.path.join(self.config.yolov5_models, "runs")

            # print(yolov5_runs)

            create_directories([runs_path])

            # best_pt = os.path.join(yolov5_runs, 'train/yolov5s_results/weights/best.pt')

            os.system(f"cp {yolov5_runs} {runs_path}")

        except Exception as e:
            raise CustomException(e, sys)
