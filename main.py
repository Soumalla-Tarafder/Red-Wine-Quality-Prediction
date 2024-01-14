from red_wine_quality_prediction import logger
from red_wine_quality_prediction.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from red_wine_quality_prediction.pipeline.stage_02_data_validation import DataValidationTrainingPipeline
from red_wine_quality_prediction.pipeline.stage_03_data_transformation import DataTransformationTrainingPipeline
from red_wine_quality_prediction.pipeline.stage_04_data_trainer import DataTranerTrainingPipeline
from red_wine_quality_prediction.pipeline.stage_05_model_evaluation import ModelEvaluationTrainingPipeline



STAGE_NAME = "Data Ingestion stage"
try:
   logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<") 
   pipeline_stage_01 = DataIngestionTrainingPipeline()
   pipeline_stage_01.main()
   logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e



STAGE_NAME = "Data Validation stage"
try:
   logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<") 
   pipeline_stage_02 = DataValidationTrainingPipeline()
   pipeline_stage_02.main()
   logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e



STAGE_NAME = "Data Transformation stage"
try:
   logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<") 
   pipeline_stage_03 = DataTransformationTrainingPipeline()
   pipeline_stage_03.main()
   logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e



STAGE_NAME = "Model Trainer stage"
try:
   logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<") 
   pipeline_stage_04 = DataTranerTrainingPipeline()
   pipeline_stage_04.main()
   logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e



STAGE_NAME = "Model evaluation stage"
try:
   logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<") 
   pipeline_stage_05 = ModelEvaluationTrainingPipeline()
   pipeline_stage_05.main()
   logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e