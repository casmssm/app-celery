FROM python:3.9-alpine

WORKDIR	/app

RUN	mkdir -p /app

RUN	pip install --upgrade pip

COPY	requirements.txt /app/

RUN	pip install -r requirements.txt

COPY	./*.py		./

EXPOSE	8888
EXPOSE  5555

CMD	["python", "/app/tasks.py"]