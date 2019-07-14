FROM alpine

RUN apk add python3-dev py3-pip build-base

RUN pip3 install -U mypy

ADD main.py .

ENTRYPOINT ["bin/ash"]
