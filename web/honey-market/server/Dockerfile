FROM selenium/standalone-chrome

WORKDIR /app
COPY . /app

ENV PYTHONUNBUFFERED=1

ENV SECRET_KEY "DAWDAW>/f258zPZX3\$%#^&*&@^#*(\$(DAWDAWDA>/f258zPZX3\$%#^&*&@^#*(\$(WDAWDAWDAWD"
ENV PORT "5000"
ENV PRODUCTION "true"
ENV ADMIN_PASSWORD "Y8P>/f258zPZX3\$%#^&*&@^#*(\$(@^!()(#))))2C2Yq%<wU9i0c~j;\\9\$&AY##LOJbiM[.G"
ENV ADMIN_USERNAME "HoneyHunter"
ENV FLAG "not_pecan{http://y2u.be/dQw4w9WgXcQ}"
ENV MOTD "Whoops, sorry, no REAL flags here. But check this cool piece of knowledge out -> https://www.fortinet.com/resources/cyberglossary/what-is-honeypot"

USER root
RUN pip install -r requirements.txt
RUN python seed.py

EXPOSE 5000

CMD ["gunicorn", "-w", "10", "-b", "0.0.0.0:5000", "main:app"]
