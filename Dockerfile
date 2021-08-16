FROM python:3.8-slim

ENV folder=/opt/venv
RUN python3 -m venv
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

WORKDIR /usr/src/app


COPY ./requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt




COPY . .
RUN pytest

