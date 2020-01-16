FROM python:3.8.1-alpine3.11
RUN apk add --update curl
COPY . app/
WORKDIR app/
RUN pip install -r requirements.txt
EXPOSE 8000
CMD python manage.py runserver 0:8000
