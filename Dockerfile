FROM python:3-alpine

RUN pip3 install requests
COPY hsk_ddns.py /opt/sh/hsk_ddns.py
COPY cron.sh /opt/sh/cron.sh

CMD sh /opt/sh/cron.sh
