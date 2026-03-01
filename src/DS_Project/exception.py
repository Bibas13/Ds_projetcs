import sys
from src.DS_Project.logger import logging


def error_message_detail(error,error_details:sys):
    _,_,exc_tb = error_details.exc_info()


    if exc_tb is None:
        return f"Error: {str(error)}"
    
    file_name = exc_tb.tb_frame.f_code.co_filename
    
    #error_message = "error occured in python script name [{0}] line number [{1}] error_message[{2}] ".format(file_name,exc_tb.tb_lineno,str(error))
    
    return (
        f"Error in script: {file_name} "
        f"at line: {exc_tb.tb_lineno} "
        f"| Message: {str(error)}"
    )
    
    

class Custom_Exception(Exception):
    def __init__(self, error_message: str,error_details:sys):
        super().__init__(error_message)
        self.error_message = error_message_detail(error_message,error_details)

    def __str__(self):
        return self.error_message
        