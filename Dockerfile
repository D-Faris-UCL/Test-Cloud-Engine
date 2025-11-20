FROM python:3.11-slim
WORKDIR /app
ENV PYTHONUNBUFFERED=1
COPY main.py .
CMD ["python", "main.py"]