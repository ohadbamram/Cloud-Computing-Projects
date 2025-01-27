FROM python:alpine3.17

WORKDIR ./

COPY stockAPI.py .

RUN pip install flask requests pymongo

ENV FLASK_APP=stockAPI.py
ENV FLASK_RUN_PORT=8000
ENV FLASK_DEBUG=1

EXPOSE 8000

CMD ["flask","run","--host=0.0.0.0","--port=8000"]



