FROM debian:bookworm-slim

RUN apt-get update && \
    apt-get install -y --no-install-recommends socat && \
    rm -rf /var/lib/apt/lists/*

COPY chall flag.txt /home/ctf/
RUN chmod +x /home/ctf/chall && \
    chmod +r /home/ctf/flag.txt && \
    useradd -ms /bin/bash ctf && \
    chown -R root:root /home/ctf

USER ctf
WORKDIR /home/ctf

EXPOSE 1338
CMD ["socat", "-T60", "TCP4-LISTEN:1338,reuseaddr,fork", "EXEC:timeout 60 ./chall"]
