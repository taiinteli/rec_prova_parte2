FROM python:3.10-slim

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

EXPOSE 8005

CMD ["fastapi", "run", "main.py", "--host", "0.0.0.0", "--port", "8005"]

