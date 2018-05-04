FROM python:3.6

ENV PYTHONUNBUFFERED 1
ENV DJANGO_ENV dev
ENV DOCKER_CONTAINER 1

RUN apt-get update && \
    apt-get install -y && \
    pip3 install uwsgi

WORKDIR /repo
COPY requirements.txt /repo/

RUN pip3 install -r /repo/requirements.txt

ADD project/ /repo/

COPY .docker/entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

CMD ["uwsgi", "--ini", "/repo/uwsgi.ini"]
