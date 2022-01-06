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