from flask import current_app

from app import db
from app.main import bp

import os, base64, shutil, errno
import threading
import time, datetime, logging

logging.basicConfig(level=logging.DEBUG, format='(%(threadName)-9s) %(message)s',)

def sayhello():
	logging.debug(f'Hello at {datetime.datetime.now().strftime("%b %d %Y %H:%M:%S")}')

def OnBoot():
  threadObj = threading.Thread(name='OnBoot', target=boot, args=[current_app._get_current_object()])
  threadObj.setDaemon(True)
  threadObj.start()

def boot(app):
    with app.app_context():      
        logging.debug(f'Starting Up at {datetime.datetime.now().strftime("%b %d %Y %H:%M:%S")}') 
        
        logging.debug('Boot... done!')

def cyclic_task(f):
    threadObj = threading.Thread(name='Cyclic_Task' , target=the_task, args=[current_app._get_current_object(), f])
    threadObj.setDaemon(True)
    threadObj.start()

def the_task(app, f):
    with app.app_context():
        while True:
            delta = datetime.timedelta(seconds=app.config['DELTA'])
            f()
            next_cycle = datetime.datetime.now()+delta
            while datetime.datetime.now() < next_cycle:
                time.sleep(1)











