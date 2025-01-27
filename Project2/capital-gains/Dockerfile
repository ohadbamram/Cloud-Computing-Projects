FROM python:alpine3.17

WORKDIR ./capital-gains
COPY ./capital-gains.py .
RUN pip install flask requests

ENV FLASK_APP=capital-gains.py
ENV FLASK_RUN_PORT=8080

EXPOSE 8080

CMD ["flask", "run", "--host=0.0.0.0", "--port=8080"]