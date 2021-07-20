FROM python:3

ENV APP /app
RUN mkdir -p $APP
WORKDIR $APP
COPY app2 $APP
COPY requirements.txt $APP/requirements.txt

RUN pip install -r requirements.txt

CMD [ "uwsgi", "--ini", "uwsgi.ini" ]