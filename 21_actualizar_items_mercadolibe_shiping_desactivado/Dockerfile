FROM python:3.6.6-slim-jessie

RUN apt-get update -y

RUN apt-get upgrade -y

ADD . /flask-app

WORKDIR /flask-app

RUN pip install -r requirements.txt

ENTRYPOINT ["python"]

CMD ["app.py"]
