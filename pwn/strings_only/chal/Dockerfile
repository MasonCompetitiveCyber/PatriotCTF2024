# sudo docker build -t strings_only .
# sudo docker run -dp 8888:8888 strings_only:latest

FROM ubuntu:18.04

RUN useradd -m ctf
WORKDIR /src
RUN apt update
RUN apt install xinetd -y

COPY ctf.xinetd /etc/xinetd.d/ctf
COPY flag.txt /
COPY run.sh /src
COPY ./bin/strings_only /src
RUN mkdir /glibc && mkdir /glibc/glibc_2.25
COPY ./glibc/glibc_2.25/* /glibc/glibc_2.25/

RUN chmod 444 /flag.txt
RUN chmod +x /src/run.sh
RUN sed -i -e 's/\r$//' /src/run.sh
RUN sed -i -e 's/\r$//' /etc/xinetd.d/ctf
RUN rm -rf /var/cache/apt/archives /var/lib/apt/lists/*

CMD ["/bin/bash", "/src/run.sh"]
EXPOSE 8888
