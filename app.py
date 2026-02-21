from src.DS_Project.logger import logging
from src.DS_Project.exception import Custom_Exception
import sys






if __name__ == "__main__":
    logging.info("the logging is executed")

    try :
        a= 1/0
    except Exception as e:
        logging.info("Error is raised ")
        raise Custom_Exception(e,sys)
