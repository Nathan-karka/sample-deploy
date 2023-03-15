# syntax=docker/dockerfile:1

FROM python:3.11-slim-buster

WORKDIR /app

COPY ./requirements.txt /app/requirements.txt

RUN apt-get update && apt-get install -y \
    gcc \
    libmariadbclient-dev \
    python3-dev 

RUN apt install docker-compose

RUN pip install -r requirements.txt

COPY . /app

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]