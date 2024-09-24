FROM python:3.9-slim

WORKDIR /app
COPY . /app

RUN pip install Flask mysql-connector-python requests

ENV DB_HOST=db
ENV DB_USER=${MYSQL_USER}
ENV DB_PASSWORD=${MYSQL_PASSWORD}
ENV DB_NAME=barcode_inventory

EXPOSE 5000

CMD ["python", "app.py"]
