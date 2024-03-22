#!/usr/bin/python
from celery import Celery
import flower
import time
import logging
import os

REDIS_HOST = str(os.environ.get('REDIS_HOST', "localhost:6379"))
DEFAULT_BROKER = f'redis://{REDIS_HOST}/0'

app = Celery('tasks', broker=DEFAULT_BROKER)

@app.task
def cadastro(nome):
    print(".")
    time.sleep(1)
    logging.warn(f'Recebido -> {nome}')
    return f'Recebido -> {nome}'

app.worker_main([
        'worker',
        '--loglevel=INFO',
        '--pool=solo'
    ])