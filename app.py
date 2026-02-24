from src.DS_Project.logger import logging
from src.DS_Project.exception import Custom_Exception
import sys

from src.DS_Project.component.data_ingestion import DataIngestion
from src.DS_Project.component.data_ingestion import DataIngestionConfig




if __name__ == "__main__":
    logging.info("the logging is executed")

    try :
        logging.info("Trying to ingest data")
        dataingestion = DataIngestion()
        dataingestion.initiate_data_ingestion()
    except Exception as e:
        logging.info("Error is raised ")
        raise Custom_Exception(e,sys) 
    
