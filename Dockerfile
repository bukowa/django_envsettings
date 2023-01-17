FROM python:3.11-slim

WORKDIR /dockerapp
COPY requirements_tests.txt requirements.txt ./
RUN pip install -r requirements_tests.txt
COPY . ./
RUN chmod +x ./runtests.py
