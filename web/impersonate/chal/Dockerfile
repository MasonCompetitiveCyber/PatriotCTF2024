FROM python:3.11-alpine

RUN apk add --no-cache --update supervisor


RUN mkdir -p /app

COPY --chown=root config/supervisord.conf /etc/supervisord.conf

WORKDIR /app

COPY app.py app.py
COPY requirements.txt requirements.txt
COPY templates templates

RUN python -m pip install -r requirements.txt


ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV FLAG="PCTF{Imp3rs0n4t10n_Iz_Sup3r_Ezz}"

RUN adduser -u 1337 --disabled-password --gecos "" ctf
RUN chown -R ctf: /app /run

EXPOSE 9999

COPY --chown=root entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh
ENTRYPOINT ["/entrypoint.sh"]
