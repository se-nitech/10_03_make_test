FROM python:slim

RUN apt -y update && apt -y install git
RUN pip install pylint flake8 bandit
RUN pip install pytest coverage

RUN apt -y install make

WORKDIR /mnt
