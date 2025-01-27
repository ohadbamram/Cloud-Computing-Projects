FROM python:alpine3.17

WORKDIR ./stocks

COPY ./app.py .

RUN pip install flask requests pymongo

ENV FLASK_APP=app.py
ENV FLASK_RUN_PORT=8000
ENV COLLECTION_NAME=stocks

EXPOSE 8000

CMD ["python","app.py"]



