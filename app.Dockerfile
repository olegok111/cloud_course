FROM python:3-bookworm

RUN apt update
RUN apt install python3-flask python3-mysqldb -y
