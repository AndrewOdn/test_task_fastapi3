FROM python:3.10-slim
MAINTAINER Andrew aka Wolf

WORKDIR .


RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt


ENV PYTHONUNBUFFERED=1
COPY . .
CMD ["python"]