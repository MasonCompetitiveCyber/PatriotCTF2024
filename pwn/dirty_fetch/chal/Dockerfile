# sudo docker build -t dirty_fetch .
# sudo docker run -dp 8886:8886 dirty_fetch:latest

FROM ubuntu@sha256:77906da86b60585ce12215807090eb327e7386c8fafb5402369e421f44eff17e

# Packages
RUN apt-get update
RUN apt-get install -y qemu qemu-system-x86 qemu-utils cpio gzip xinetd bzip2 flex
RUN rm -rf /var/lib/apt/lists/*

# Low priv user
RUN useradd -d /home/ctf -m -p ctf -s /bin/bash ctf
RUN echo "ctf:ctf" | chpasswd
RUN ulimit -c 0

# xinetd
COPY ctf.xinetd /etc/xinetd.d/ctf
COPY run.sh /src/run.sh
RUN chmod +x /src/run.sh
RUN sed -i -e 's/\r$//' /src/run.sh
RUN sed -i -e 's/\r$//' /etc/xinetd.d/ctf

# Qemu system
COPY start.sh /src/start.sh
RUN chmod +x /src/start.sh
COPY helper_scripts/linux-5.4/arch/x86/boot/bzImage /src/bzImage
COPY initramfs.cpio.gz /src/initramfs.cpio.gz

CMD ["/bin/bash","/src/run.sh"]
EXPOSE 8886
