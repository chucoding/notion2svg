import logging, logging.config
import json
import os, os.path

class logMng:
    def __init__(self):
        pass
        
    def get_logger(self, _name):
        if not os.path.exists('logs/'):
            os.makedirs('logs/')
        
        curr_path = os.getcwd()
        with open(curr_path+"\\utils\\logMng.json", "rt") as file:
            config = json.load(file)

        logging.config.dictConfig(config)
        __logger = logging.getLogger(_name)

        return __logger

if __name__ == '__main__':
    logger = logMng.get_logger("test")
    logger.info("TEST...!!!")