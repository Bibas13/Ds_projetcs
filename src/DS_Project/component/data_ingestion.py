import pandas as pd

import os
import sys

from src.DS_Project.logger import logging
from src.DS_Project.exception import Custom_Exception

from sklearn.model_selection import train_test_split

from src.DS_Project.utils import read_sql_data

from dataclasses import  dataclass

#in this stage 
#read data from --> sql and train test split


@dataclass 
class DataIngestionConfig:
    train_data_path:str = os.path.join("artifacts","train.csv")
    test_data_path:str = os.path.join("artifacts","test.csv")
    raw_data_path:str = os.path.join("artifacts","raw.csv")


class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()

    def initiate_data_ingestion(self):
        
        try:
            #reading code
            df1 = read_sql_data()
            logging.info("reading completed from mysql database")
            if df1 is None:
                raise ValueError("Query returned None")
            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path),exist_ok = True)
            #reading from mysql

            df1.to_csv(self.ingestion_config.raw_data_path,index = False,header = True)
            train_set ,test_set = train_test_split(df1,test_size = 0.2,random_state= 42)
            train_set.to_csv(self.ingestion_config.train_data_path,index=False,header=True)
            test_set.to_csv(self.ingestion_config.test_data_path,index=False,header=True)
            
            logging.info("data ingestion is complete")


            return(
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )

            


        except Exception as e:
            raise Custom_Exception(e,sys) from e
        
    

