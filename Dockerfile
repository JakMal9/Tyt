
FROM python:3.8

ADD weltyt.py /
ADD TYTDB.sql /

CMD [ "python", "./weltyt.py" ]
