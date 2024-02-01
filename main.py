
import os,sys
from pathlib import Path

from waste_detection.logger import logging
from waste_detection.exception import CustomException


from waste_detection.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from waste_detection.pipeline.stage_02_data_validation import DataValidationTrainingPipeline



stage_name = "Data Ingestion"
try:
    logging.info(f">>>>>>>>>>>>>>>>> {stage_name} Started <<<<<<<<<<<<<<<<<<< ")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logging.info(f">>>>>>>>>>>>>>>>> {stage_name} Completed <<<<<<<<<<<<<<<<<<< ")

except Exception as e:
    logging.error(f">>>>>>>>>>>>>>>>> {stage_name} Failed <<<<<<<<<<<<<<<<<<< ")
    raise CustomException(e,sys)





stage_name = "Data Validation"
try:
    logging.info(f">>>>>>>>>>>>>>>>> {stage_name} Started <<<<<<<<<<<<<<<<<<< ")
    data_validation = DataValidationTrainingPipeline()
    data_validation.main()
    logging.info(f">>>>>>>>>>>>>>>>> {stage_name} Completed <<<<<<<<<<<<<<<<<<< ")

except Exception as e:
    logging.error(f">>>>>>>>>>>>>>>>> {stage_name} Failed <<<<<<<<<<<<<<<<<<< ")
    raise CustomException(e,sys)





