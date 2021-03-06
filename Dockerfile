FROM ubuntu:latest
MAINTAINER "Ciaran admin@cturtle98.com"

RUN apt update
RUN apt upgrade -y
RUN apt install -y python3-pip python3-dev build-essential iproute2
RUN pip3 install flask
COPY door.py /app/web.py
COPY html/ /app/html/
WORKDIR /app
ENTRYPOINT ["python3"]
CMD ["web.py"]
