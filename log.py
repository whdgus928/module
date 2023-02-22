from selenium import webdriver
from selenium.webdriver.common.by import By
import os
import chromedriver_autoinstaller as AutoChrome
import datetime
import time
from selenium.webdriver import ActionChains
from logging.config import dictConfig
import logging
import traceback
import re

def log(msg):
    logging.info(msg)
class LoopBreak(Exception):
    pass
filePath, fileName = os.path.split(__file__)
logFolder = os.path.join(filePath , 'logs')
os.makedirs(logFolder, exist_ok = True)
logfilepath = os.path.join(logFolder, fileName.split('.')[0] + '_' +re.sub('-', '', str(datetime.date.today())) + '.log')
dictConfig({
    'version': 1,
    'formatters': {
        'default': {
            'format': '[%(asctime)s] %(levelname)s --- %(message)s',
        }
    },
    'handlers': {
        'file': {
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'filename': logfilepath,
            'formatter': 'default',
        },
    },
    'root': {
        'level': 'INFO',
        'handlers': ['file']
    }
})              

log('test')