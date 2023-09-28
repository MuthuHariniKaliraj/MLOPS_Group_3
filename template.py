''' 
    Creates the folder structure 
'''

import os 
import logging 
from pathlib import Path

# logging information at a specified path 
dir_name = 'logs'
os.makedirs(dir_name,exist_ok=True)
log_path = os.path.join(dir_name,'logging_data.log')
logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s', 
                    handlers= [ logging.FileHandler(log_path)] 
                    )
project_name = 'mlops_stellar' 

# List of folders, files that are needed
list_of_files = [
    '.github/workflows/.gitkeep',
    f'src/{project_name}/__init__.py',
    f'src/{project_name}/components/__init__.py',
    f'src/{project_name}/utils/__init__.py',
    f'src/{project_name}/utils/common.py',
    f'src/{project_name}/logging/__init__.py',
    f'src/{project_name}/config/__init__.py',
    f'src/{project_name}/config/configuration.py',
    f'src/{project_name}/pipeline/__init__.py',
    f'src/{project_name}/entity/__init__.py',
    f'src/{project_name}/constants/__init__.py',
    'config/config.yaml',
    'params.yaml',
    'app.py',
    'Dockerfile',
    'requirements.txt',
    'setup.py',
    
]

'''
    Creating a CI/CD pipeline 
'''

for filepath in list_of_files:
    # converting filepath into windows version 
    filepath = Path(filepath) 
    filedir, filename = os.path.split(filepath) 
    if filedir != "":
        os.makedirs(filedir, exist_ok=True) 
        logging.info(f'creating directory:{filedir} for the file {filename}') 
   
    
    
    # if there is no path with the filepath then creating it 
    # if the size of the specified filepath = 0 then create the file 

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) ==0) : 
        with open(filepath, 'w') as f:
            pass 
            logging.info(f'creating empty file: {filepath}')
    else:
        logging.info(f'{filename} already exists')


    

