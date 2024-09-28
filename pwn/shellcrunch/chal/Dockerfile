# docker build -t shellcrunch .
# docker run -dp 3004:3004 shellcrunch:latest

FROM ubuntu@sha256:77906da86b60585ce12215807090eb327e7386c8fafb5402369e421f44eff17e

RUN useradd -m ctf
WORKDIR /src
RUN apt update
RUN apt install xinetd -y

COPY ctf.xinetd /etc/xinetd.d/ctf
COPY flag.txt /flag.txt
COPY run.sh /src/run.sh
COPY shellcrunch /src/shellcrunch

RUN chmod 444 /flag.txt
RUN chmod +x /src/run.sh
RUN sed -i -e 's/\r$//' /src/run.sh
RUN sed -i -e 's/\r$//' /etc/xinetd.d/ctf
RUN rm -rf /var/cache/apt/archives /var/lib/apt/lists/*

CMD ["/bin/bash","/src/run.sh"]
EXPOSE 3004
