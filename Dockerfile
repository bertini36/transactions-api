FROM python:3.8

WORKDIR /code/

RUN apt update \
 && apt install -y libjpeg-dev libgraphviz-dev libpq-dev build-essential \
 && apt install -y libxmlsec1-dev pkg-config graphviz graphicsmagick python-dev gettext

COPY requirements/dev.txt requirements.txt

RUN pip3 install --upgrade pip  && pip3 install -r requirements.txt
