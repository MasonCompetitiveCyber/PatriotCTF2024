# sudo docker build -t navigator .
# sudo docker run -dp 8887:8887 --privileged navigator:latest

FROM ubuntu@sha256:77906da86b60585ce12215807090eb327e7386c8fafb5402369e421f44eff17e

RUN useradd -m ctf
WORKDIR /src
RUN apt update
RUN apt install xinetd -y

COPY ctf.xinetd /etc/xinetd.d/ctf
COPY flag.txt /
COPY run.sh /src
COPY ./navigator /src

RUN chmod 444 /flag.txt
RUN chmod +x /src/run.sh
RUN sed -i -e 's/\r$//' /src/run.sh
RUN sed -i -e 's/\r$//' /etc/xinetd.d/ctf
RUN rm -rf /var/cache/apt/archives /var/lib/apt/lists/*

CMD ["/bin/bash","/src/run.sh"]
EXPOSE 8887
