import pandas as pd
import os, sys
from pathlib import Path
from ensure import ensure_annotations

import yaml
import json

# import joblib
# import pickle

from box import ConfigBox

from typing import Any

import base64

from waste_detection.logger import logging
from waste_detection.exception import CustomException


@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """Read a yaml file and return a ConfigBox object.

    Parameters:
    path_to_yaml : Path

    Returns:
    ConfigBox

    """

    try:
        path_to_yaml = Path(path_to_yaml)
        with open(path_to_yaml, "r") as yaml_file:
            content = yaml.safe_load(yaml_file)
            logging.info(f"yaml file: {path_to_yaml} loaded successfully.")
            return ConfigBox(content)

    except Exception as e:
        logging.error(f"Error occured while reading yaml file: {path_to_yaml}")
        raise CustomException(e, sys)



def read_modify_write_yaml(input_file_path, output_file_path, changes):
    try:
        # Read YAML file
        with open(input_file_path, 'r') as file:
            yaml_content = yaml.safe_load(file)

        # Modify key-value pairs
        for key, value in changes.items():
            yaml_content[key] = value

        # Write modified content to a new file
        with open(output_file_path, 'w') as file:
            yaml.dump(yaml_content, file)

    except Exception as e:
        print(f"Error occurred: {e}")



@ensure_annotations
def create_directories(path_to_directories: list, verbose=True):
    """
    Creates list of directories

    Arguments: path_to_directories

    """

    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)

        if verbose:
            logging.info(f"Created Directory at {path}.")


@ensure_annotations
def save_csv(path: Path, data: pd.DataFrame):
    """
    save csv data

    Args:
    path(Path): path to save csv
    data(pd.DataFrame): data to be save to csv file

    """
    data.to_csv(path, index=False)
    logging.info(f"csv file saved at: {path}.")
    # return path


@ensure_annotations
def save_json(path: Path, data: dict):
    """
    save json data

    Args:
    path(Path): path to save json
    data(dict): data to be save to json file

    """
    with open(path, "w") as f:
        json.dump(data, f, indent=4)

    logging.info(f"json file saved at: {path}.")


@ensure_annotations
def load_json(path: Path) -> ConfigBox:
    """load json files data

    Args:
        path (Path): path to json file

    Returns:
        ConfigBox: data as class attributes instead of dict
    """
    with open(path) as f:
        content = json.load(f)

    logging.info(f"json file loaded succesfully from: {path}")
    return ConfigBox(content)


def decodeImage(imgstring, fileName):
    imgdata = base64.b64decode(imgstring)
    with open("./data/" + fileName, "wb") as f:
        f.write(imgdata)
        f.close()


def encodeImageIntoBase64(croppedImagePath):
    with open(croppedImagePath, "rb") as f:
        return base64.b64encode(f.read())


# import yaml


def update_yaml_file(file_path, key_path, new_value):
    try:
        # Load YAML file
        with open(file_path, "r") as file:
            data = yaml.safe_load(file)

        # Update the value using the key path
        nested_dict = data
        keys = key_path.split(".")
        for key in keys[:-1]:
            nested_dict = nested_dict[key]
        nested_dict[keys[-1]] = new_value

        # Save the updated YAML back to the file
        with open(file_path, "w") as file:
            yaml.dump(data, file, default_flow_style=False)

        logging.info(f"Updated '{key_path}' to '{new_value}' in '{file_path}'.")
    except Exception as e:
        logging.info(f"Error updating YAML file: {e}")
        raise CustomException(e,sys)

# # Example usage
# yaml_file_path = "example.yaml"
# key_to_update = "some.nested.key"
# new_value_to_set = "new_value"

# update_yaml_file(yaml_file_path, key_to_update, new_value_to_set)
