FROM python:3.10

RUN apt-get update && apt-get install -y nginx

WORKDIR /app

ADD . /app

RUN mkdir -p /etc/nginx/certs/

COPY ./certs/cert.pem /etc/nginx/certs/cert.pem
COPY ./certs/key.pem /etc/nginx/certs/key.pem

COPY nginx.conf /etc/nginx/nginx.conf

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]
