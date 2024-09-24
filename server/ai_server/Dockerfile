FROM python:3.8-slim

WORKDIR /app

COPY ai_server.py /app/
COPY requirements.txt /app/

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5001

CMD ["python", "ai_server.py"]
