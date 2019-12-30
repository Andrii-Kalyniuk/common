# pull official base image
FROM python:3.8.0-alpine

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install psycopg2 dependencies
RUN apk update \
    && apk add postgresql-dev gcc python3-dev musl-dev

# copy project
COPY . /usr/src/app/
# install dependencies

# set work directory
WORKDIR /usr/src/app

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

CMD python manage.py create_db
