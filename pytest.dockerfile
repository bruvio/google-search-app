FROM python:3.8-slim
MAINTAINER bruvio

COPY ./requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

RUN pip install pytest

ENTRYPOINT [ "pytest","/usr/src/app/tests" ]
