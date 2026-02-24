
import os
import sys


from src.DS_Project.logger import logging
from src.DS_Project.exception import Custom_Exception

import pandas as pd

import pymysql

from dotenv import load_dotenv

load_dotenv()
host=os.getenv("host")
user = os.getenv("user")
password = os.getenv("password")
db = os.getenv("db")



def read_sql_data():
    logging.info("Reading sql database started")

    try:
        my_db = pymysql.connect(
            host=host,
            user=user,
            password=password ,
            db=db
        )
        logging.info(f"Connection Established {my_db}")


        df = pd.read_sql_query("Select * FROM StudentsPerformance",my_db)
        

        print(df.head())
        
        return df

    except Exception as ex:
        raise Custom_Exception(ex,sys) from ex
