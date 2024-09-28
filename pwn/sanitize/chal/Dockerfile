# sudo docker build -t sanitizer .
# sudo docker run -dp 5001:5001 --privileged sanitizer:latest

FROM ubuntu@sha256:77906da86b60585ce12215807090eb327e7386c8fafb5402369e421f44eff17e

RUN useradd -m ctf
WORKDIR /src
RUN apt update
RUN apt -y install xinetd qemu-user qemu-user-binfmt libc6-mipsel-cross gcc-mipsel-linux-gnu


COPY ctf.xinetd /etc/xinetd.d/ctf
COPY flag.txt /
COPY run.sh /src
COPY ./urltools /src
COPY ./run_challenge.sh /src

RUN chmod 444 /flag.txt
RUN chmod +x /src/run.sh
RUN sed -i -e 's/\r$//' /src/run.sh
RUN sed -i -e 's/\r$//' /etc/xinetd.d/ctf
RUN rm -rf /var/cache/apt/archives /var/lib/apt/lists/*

CMD ["/bin/bash","/src/run.sh"]
EXPOSE 5001
