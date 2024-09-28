# sudo docker build -t badblood .
# sudo docker run -dp 10001:1337 badblood:latest

FROM ubuntu:latest

RUN apt update -y \
    && apt install python3 -y

# COPY challenge
COPY checker.py /opt/checker.py
COPY external.py /opt/external.py

RUN rm -rf /var/cache/apt/archives /var/lib/apt/lists/*

EXPOSE 10001

CMD ["python3","/opt/checker.py"]
