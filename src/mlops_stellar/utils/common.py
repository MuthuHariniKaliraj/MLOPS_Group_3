"""
    Here we will put those codes which can be later 
    used as a package i.e. re-usable functions
"""

import os 
import yaml 
from src.mlops_stellar import logger 
from pathlib import Path
from box import ConfigBox
from ensure import ensure_annotations 
from box.exceptions import BoxValueError 



# the decorator makes sure to handle the input type correctly
# e.g. if its int, it makes sure you pass integer variable only
@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """
        @Parameters:
            path_to_yaml (str): path of the yaml file 
        @does:
            reads the yaml files and returns the necessary outputs
        @Returns:
            ConfigBox: ConfigBox type [dictionary elements are accessed in the form of list format]
    """
    try:
        with open(path_to_yaml) as yaml_file:
            context = yaml_file.safe_load(yaml_file) 
            logger.info(f'yaml file loaded successfully: {path_to_yaml}')
        return ConfigBox(context) 
    except BoxValueError:
        raise ValueError('yaml file empty') 
    except Exception as e:
        raise e 
    
@ensure_annotations
def create_directories(path_to_directories: list, verbose=True):
    """
        @Parameters:
            path_to_directories (list): list of the paths for directory files
        @does:
            reads the yaml files and returns the necessary outputs
        @Returns:
            ConfigBox: ConfigBox type [dictionary elements are accessed in the form of list format]
    """

    for path in path_to_directories:
        os.makedirs(path, exist_ok=True) 
        if verbose:
            logger.info(f'created directory : {path}') 

            