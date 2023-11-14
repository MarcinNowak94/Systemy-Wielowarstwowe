# syntax=docker/dockerfile:1
#https://www.freecodecamp.org/news/how-to-dockerize-a-flask-app/

FROM python:3.8-slim-buster
WORKDIR /app
#requirements.txt content: Flask
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
COPY . .
#startscript.sh content: python3 -m flask run
CMD ./startscript.sh
EXPOSE 8000