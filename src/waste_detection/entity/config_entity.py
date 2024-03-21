
from dataclasses import dataclass
from pathlib import Path

@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir: Path
    feature_path: Path
    data_URL: Path
    data_path: Path


@dataclass(frozen=True)
class DataValidationConfig:
    # root_dir: Path
    # status: Path
    data_yaml: Path
    train_path: Path
    valid_path: Path



@dataclass(frozen=True)
class ModelTrainingConfig:
    root_dir: Path
    yolov5_root: Path
    yolov5_models: Path
    custom_yolov5: Path
    train_path: Path
    yolov5_runs: Path
    history: Path
    git_URL: str
    IMAGE_SIZE: int
    BATCH_SIZE: int
    EPOCHS: int
    DATA: Path
    WEIGHTS: str
    NAME: str



