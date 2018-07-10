FROM python:2.7

WORKDIR /root/

RUN apt-get update \
    && apt-get install -y  gcc g++ \
    && apt-get install -y  libsasl2-dev libldap2-dev \
    && pip install python-ldap==2.4.22 \
    && pip install requests

COPY grafana_sync.py grafana_sync.py

ENTRYPOINT python /root/grafana_sync.py