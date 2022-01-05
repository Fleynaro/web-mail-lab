FROM python:3.7

RUN mkdir /server
WORKDIR /server

COPY ./requirements.txt ./
RUN pip install -r requirements.txt

COPY ./mail ./mail
COPY ./shared ./shared
COPY ./temp ./temp

COPY ./start_mail_server.py ./

EXPOSE 8081
ENTRYPOINT ["python", "./start_mail_server.py"]