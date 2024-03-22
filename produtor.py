from celery import Celery
import flower
import time
import logging
import os

import celery_prometheus_exporter

REDIS_HOST = str(os.environ.get('REDIS_HOST', "localhost:6379"))

SAMPLE = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "x", "z"]

COUNTER = 0

app = Celery('tasks', broker=f'redis://{REDIS_HOST}/0')

@app.task
def cadastro(nome):
    time.sleep(1)
    return f'Enviado -> {nome}'

def main():
    global COUNTER
    logging.warning('Starting producer...')
    for ITEM in SAMPLE:
        MSG = f'{ITEM},{COUNTER}'
        cadastro.delay(f'cadastro_item({MSG})')
        logging.warning(f"Sending: {MSG}")
    COUNTER += 1

while True:
    main()
    time.sleep(len(SAMPLE))