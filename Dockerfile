# base image
FROM python:3.10.3-slim-buster

# set working dir
WORKDIR /usr/src/app

# set enviroment variables
ENV PYTHONDONTWRITEBYTECODE 1
# Prevents Python from writing pyc files to disc (equivalent to python -B option)
ENV PYTHONUNBUFFERED 1
# Prevents Python from buffering stdout and stderr (equivalent to python -u option)

# install system dependencies
RUN apt-get update \
    && apt-get -y install netcat gcc postgresql \
    && apt-get clean

# add and install requirments
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# add app
COPY . .

# run server
COPY ./entrypoint.sh .
RUN chmod +x /usr/src/app/entrypoint.sh