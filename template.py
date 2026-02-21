import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO)

project_name = "DS Project"

list_of_files = [
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/component/__init__.py",
    f"src/{project_name}/component/data_ingestion.py",
    f"src/{project_name}/component/data_transformation.py",
    f"src/{project_name}/component/model_training.py",
    f"src/{project_name}/component/model_monitoring.py",
    #f"src/{project_name}/component/model_evaluation.py"
    f"src/{project_name}/pipelines/__init__.py",
    f"src/{project_name}/pipelines/training_pipeline.py",
    f"src/{project_name}/pipelines/prediction_pipeline.py",
    f"src/{project_name}/exception.py",
    f"src/{project_name}/logger.py",
    f"src/{project_name}/utils.py",
    "app.py",
    "main.py",
    "requirement.txt",
    "setup.py",
    "Dockerfile"
    


]


for file_path in list_of_files:
    file_path = Path(file_path)
    filedir , filename = os.path.split(file_path)

    if filedir != "":
        os.makedirs(filedir,exist_ok=True)
        logging.info(f"created the file directory: {filedir} for file: {filename}")


    if (not os.path.exists(file_path) or (os.path.getsize(file_path == 0 ))):
        with open (file_path,'w') as f:
            pass
            logging.info(f"empty the file directory  is created :{file_path}")
        
    else:
        logging.info(f"file  {file_path} path exits" )
