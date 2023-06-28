FROM debian:latest

WORKDIR /

COPY ./dqr ./dqr

RUN mkdir ./static
RUN mkdir ./db


RUN apt update
RUN apt install -y python3 python3-pip

RUN pip3 install -r ./dqr/requirements.txt --break-system-packages
RUN python3 dqr/manage.py collectstatic --noinput