# sudo docker build -t making-baking-pancakes . && sudo docker run -dp 9001:1337 making-baking-pancakes:latest

FROM ubuntu:latest

RUN apt update -y \
    && apt install python3 -y \
    && apt install python3-pip -y

# COPY challenge
COPY runner.py /opt/runner.py
COPY external.py /opt/external.py

# Install libraries
RUN pip3 install pycryptodome --break-system-packages

RUN rm -rf /var/cache/apt/archives /var/lib/apt/lists/*

EXPOSE 9001

CMD ["python3","/opt/runner.py"]
