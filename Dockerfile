FROM python:3.14-slim

WORKDIR /app

COPY app/ .

RUN pip install flask prometheus-client

EXPOSE 5000

CMD ["python", "main.py"]