FROM python:3.7.9-buster

WORKDIR /usr/src/app

RUN apt-get update && apt-get install apt-file -y && apt-file update && apt-get install vim -y

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

