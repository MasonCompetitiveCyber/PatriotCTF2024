# docker build -t schnorr .
# docker run -it -dp 6003:1337 schnorr


# Use an official Ubuntu base image
FROM ubuntu:22.04

# Set environment variables
ENV DEBIAN_FRONTEND=noninteractive

# Install necessary packages including SageMath and socat
RUN apt-get update && apt-get install -y \
    sagemath \
    sagemath-doc \
    sagemath-jupyter \
    socat \
    python3-pip \
    && apt-get clean

# Install any additional Python dependencies
RUN pip3 install --no-cache-dir tqdm pwntools

# Expose port 1337 to listen for incoming connections
EXPOSE 1337

# Copy the challenge file into the container
COPY chall.py /app/server.py
COPY flag.txt /app/flag.txt

# Clean apt
RUN rm -rf /var/cache/apt/archives /var/lib/apt/lists/*

# Set the working directory
WORKDIR /app

# Run the socat command to listen on port 1337 and execute the SageMath Python challenge
CMD socat TCP-LISTEN:1337,reuseaddr,fork EXEC:"sage -python /app/server.py",pty,stderr,setsid,sigint,sane
