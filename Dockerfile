FROM python:3.8-slim

ENV VIRTUAL_ENV=/opt/venv
RUN python3 -m venv $VIRTUAL_ENV

ENV PATH="$VIRTUAL_ENV/bin:$PATH"

WORKDIR /usr/src/app


COPY ./requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt




COPY . .
EXPOSE 8000

# runs the production server
ENTRYPOINT ["python", "search_engine-project/manage.py"]
CMD ["runserver", "0.0.0.0:8000"]
