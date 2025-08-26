FROM python:3.13-slim

WORKDIR /usr/src/app

RUN pip install --no-cache-dir bcrypt asyncssh quart aiomqtt redis

COPY src .

EXPOSE 43713

CMD [ "python", "./gate.py" ]

