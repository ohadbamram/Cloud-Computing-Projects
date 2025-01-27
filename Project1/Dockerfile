FROM python:alpine3.17

WORKDIR ./

COPY stockAPI.py .

RUN pip install flask
RUN pip install requests

ENV FLASK_APP=stockAPI.py
ENV FLASK_RUN_PORT=5001
ENV FLASK_DEBUG=1

EXPOSE 5001

CMD ["flask","run","--host=0.0.0.0","--port=5001"]



