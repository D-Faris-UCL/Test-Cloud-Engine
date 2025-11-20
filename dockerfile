FROM python:3.11-slim
WORKDIR /app
COPY job.py .
CMD ["python", "main.py"]