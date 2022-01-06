FROM tiangolo/uwsgi-nginx-flask:python3.8

WORKDIR /app

COPY ./requirements.txt ./
RUN pip install -r requirements.txt

COPY ./mail ./mail
COPY ./shared ./shared
COPY ./temp ./temp

COPY ./start_mail_server.py ./main.py
RUN mv ./mail/uwsgi.ini ./uwsgi.ini

ENV URL_PREFIX /labs/mail



# useful
# https://hub.docker.com/r/tiangolo/uwsgi-nginx-flask/ (Quick Start)
# https://www.digitalocean.com/community/tutorials/how-to-build-and-deploy-a-flask-application-using-docker-on-ubuntu-18-04-ru