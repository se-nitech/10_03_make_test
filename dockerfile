FROM python:slim

RUN pip install pylint flake8 coverage \
    && apt -y update \
    && apt -y install git make

WORKDIR /mnt/10_03_make_test
