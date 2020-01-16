FROM python:3
MAINTAINER shivanand3939@gmail.com

RUN apt-get update
COPY . /app
WORKDIR /app

RUN pip install -r requirements.txt

EXPOSE 5001

CMD ["python","./app.py"]
