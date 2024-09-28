# sudo docker build -t hard_to_implement .
# sudo docker run -dp 6001:1337 hard_to_implement:latest

FROM ubuntu:latest

RUN apt update -y \
    && apt install python3 -y \
    && apt install python3-pip -y

# COPY challenge
COPY cryptor.py /opt/cryptor.py
COPY external.py /opt/external.py

# Install libraries
RUN pip3 install pycryptodome --break-system-packages

RUN rm -rf /var/cache/apt/archives /var/lib/apt/lists/*

EXPOSE 6001

CMD ["python3","/opt/cryptor.py"]
