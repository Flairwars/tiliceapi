FROM python:3
COPY ./requirements.txt /app/requirements.txt
WORKDIR /app
RUN pip install -r requirements.txt
COPY ./src /app/src
CMD ["python", "-m", "app"]