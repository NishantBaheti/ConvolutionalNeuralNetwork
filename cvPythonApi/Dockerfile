FROM python:3.8-slim-buster

WORKDIR /app

COPY . /app

RUN pip --no-cache-dir install -r requirements.txt

EXPOSE 5443

ENTRYPOINT ["gunicorn","--certfile ./cert/cvapp.crt","--keyfile ./cert/cvapp.key","-b 0.0.0.0:5443","-w 4","app:app"]


# ENTRYPOINT ["gunicorn","--certfile ./cert/cvapp.crt", "--keyfile ./cert/cvapp.key" ,"-b 0.0.0.0:5443","-w 4","app:app"]


# docker build -t cvpythonapi:1.0.0 . 
# docker container run -it -d -p 8080:8081 --name cvpythonapi cvpythonapi:1.0.0
