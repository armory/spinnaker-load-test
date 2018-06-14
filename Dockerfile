FROM python:3.6.5

RUN pip install --upgrade pip && pip install \
    locustio

ADD src/ /app
