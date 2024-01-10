FROM python:3.10-slim-buster

RUN apt-get update && apt-get install -y nginx

WORKDIR /app

ADD . /app

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 80

CMD ["sh", "-c", "service nginx start && python main.py"]
