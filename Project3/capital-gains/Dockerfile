FROM python:alpine3.17

WORKDIR ./capital-gains
COPY ./app.py .
RUN pip install flask requests

ENV FLASK_APP=app.py
ENV FLASK_RUN_PORT=8080

EXPOSE 8080

CMD ["python", "app.py"]
