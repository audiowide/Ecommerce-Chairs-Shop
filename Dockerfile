FROM python:3.10

RUN mkdir code
WORKDIR code

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

ADD . /code/
ADD .env.docker /code/.env

ENV APP_NAME=CHAIRS_SHOP

COPY . .
CMD gunicorn demo.wsgi:application -b 0.0.0.0:8080