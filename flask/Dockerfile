FROM python:3
COPY requirements.txt /
RUN apt-get update && apt-get upgrade -y
RUN pip3 install -r /requirements.txt
COPY . /app
WORKDIR /app
RUN chmod +x gunicorn.sh
ENTRYPOINT ["./gunicorn.sh"]