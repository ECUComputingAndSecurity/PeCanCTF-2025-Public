FROM debian:bookworm-slim

RUN apt-get update && \
    apt-get install -y --no-install-recommends socat && \
    rm -rf /var/lib/apt/lists/*

COPY EchoChamber flag.txt /home/ctf/
RUN chmod +x /home/ctf/EchoChamber && \
    chmod +r /home/ctf/flag.txt && \
    useradd -ms /bin/bash ctf && \
    chown -R root:root /home/ctf

USER ctf
WORKDIR /home/ctf

EXPOSE 1337
CMD ["socat", "-T60", "TCP4-LISTEN:1337,reuseaddr,fork", "EXEC:timeout 60 ./EchoChamber"]
