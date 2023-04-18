FROM python:3
COPY ./app.py 	./
COPY ./requirements.txt	./
RUN pip install --upgrade pip --no-cache-dir
RUN pip install -r /requirements.txt --no-cache-dir
CMD [“./gunicorn.sh”]