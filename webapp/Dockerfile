FROM python:3.6-alpine

RUN mkdir /data/

RUN apk update && apk add gcc tzdata g++ make pkgconfig

ENV TZ=America/Recife

######################################################
#   Adding user and changing current directory
######################################################

RUN adduser -D hmv
WORKDIR /home/hmv

######################################################
#   pip install python deps from requirements.txt
#   For caching until requirements.txt changes
######################################################

COPY requirements.txt requirements.txt
RUN python -m venv venv
RUN venv/bin/pip install -r requirements.txt

######################################################
#   Copy source code into a container directory
######################################################

COPY app app
COPY project.py config.py start.sh .env ./
RUN chmod a+x start.sh

######################################################
#   Environment Variables
######################################################

ENV FLASK_APP project.py

RUN chown -R hmv:hmv ./
USER hmv

######################################################
#   run python script when container lands on device
######################################################

ENTRYPOINT ["./start.sh"]
