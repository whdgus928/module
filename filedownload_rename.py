import os
import traceback
import time
import logging
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

from logging.config import dictConfig
import datetime

import re
filePath, fileName = os.path.split(__file__)
logFolder = os.path.join(filePath , 'logs')
os.makedirs(logFolder, exist_ok = True)
logfilepath = os.path.join(logFolder, fileName.split('.')[0] + '_' + re.sub('-', '', str(datetime.date.today())) + '.log')
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


def log(msg):
    logging.info(msg)

#경로 안에 있는 파일 리스트 리턴
def read_filelist(path):
    try:
        log('#### Read path {}'.format(path))
        file_list = list([])
        for dirpath, _, filenames in os.walk(path):
            for f in filenames:
                try:
                    file_list.append(os.path.abspath(os.path.join(dirpath, f)))
                except:
                    log('######## Read file error : {}'.format(filenames))
                    log('############ {}'.format(traceback.format_exc()))
        return file_list
    except:
        log('#### Read file list error')
        log('######## {}'.format(traceback.format_exc()))


def rename_file(path, new_file_name):
    try:
        while True:
            time.sleep(1)
            if len(read_filelist(path)) == 0:
                continue
            else:
                file_name = max([path + '/' + f for f in os.listdir(path)], key=os.path.getmtime)
                if '한국독서능력검정' not in file_name:
                    continue
                else :
                    print(f'######## Success to find : {file_name}')
                    break
        os.rename(file_name, path + '/' + new_file_name)
        print(f'######## Success to Rename {new_file_name}')
        log('######## ERROR : d')
        log(traceback.format_exc())
    except :
        print('#### Rename file list error')
        print('######## {}'.format(traceback.format_exc()))


filePath = os.getcwd().replace('\\','/')
driver_path ='C:\\Users\\user\\Desktop\\VS code\\test\\chromedriver.exe'
try :
    driver = webdriver.Chrome(driver_path)
except :
    print('######## Chrome Driver Error')
try :
    driver.get('https://kbooktest.bookcosmos.com/sub/book/paper_download.asp')
except :
    print('#### Get URL Error')
try :
    driver.get('/html/body/table/tbody/tr/td[1]/div[2]/dt[1]/a/img')
except :
    print('#### Get list Error')


for i in range(2,13):
    target = driver.find_element(by=By.XPATH, value= f'/html/body/table/tbody/tr/td[2]/table[1]/tbody/tr/td/table/tbody/tr[{i}]/td[1]/a')
    target.click()
    time.sleep(2)
    rename_file('C:\\Users\\user\\Downloads',f'book{i}.pdf')
