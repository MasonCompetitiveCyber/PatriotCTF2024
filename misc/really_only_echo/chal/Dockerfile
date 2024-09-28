# sudo docker build -t really_only_echo .
# sudo docker run -dp 3333:3333 really_only_echo:latest

FROM ubuntu:latest

RUN apt update -y \
    && apt install python3 -y

COPY server.py /opt/server.py
COPY flag.txt /flag.txt
RUN chown root: /flag.txt
RUN chmod +r /flag.txt

RUN useradd -m ctf

RUN rm -rf /var/cache/apt/archives /var/lib/apt/lists/*

USER ctf

EXPOSE 3333

CMD ["python3","/opt/server.py"]
