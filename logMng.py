import logging, logging.config
import json
import os, os.path

def get_logger(_name):
    if not os.path.exists('logs/'):
        os.makedirs('logs/')
    
    with open("logMng.json", "rt") as file:
        config = json.load(file)

    logging.config.dictConfig(config)
    __logger = logging.getLogger(_name)

    return __logger

if __name__ == '__main__':
    logger = get_logger("test")
    logger.info("TEST...!!!")