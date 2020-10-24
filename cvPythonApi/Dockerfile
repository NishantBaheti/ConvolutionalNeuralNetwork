FROM python:3.8-slim-buster

WORKDIR /app

COPY . /app

RUN pip --no-cache-dir install -r requirements.txt

EXPOSE 8081

ENTRYPOINT ["gunicorn","-b 0.0.0.0:8081","-w 4","app:app"]


# docker build -t cvpythonapi:1.0.0 . 
# docker container run -it -d -p 8080:8081 --name cvpythonapi cvpythonapi:1.0.0
