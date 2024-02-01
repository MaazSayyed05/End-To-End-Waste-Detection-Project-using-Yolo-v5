
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





