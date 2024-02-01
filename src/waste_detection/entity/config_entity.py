
from dataclasses import dataclass
from pathlib import Path

@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir: Path
    feature_path: Path
    data_URL: Path
    data_path: Path




