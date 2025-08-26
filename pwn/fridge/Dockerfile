# If you like, you can work on this locally by running something like:
# docker build -t pecanfridge .
# docker run -d -p 1358:1358 --name pecanfridge pecanfridge
#
# Then, you can just 'nc localhost 1358' to mess around with it on your own computer!
#
# You might need to add --platform linux/amd64 to each of those commands if you are 
# trying to run it on an ARM machine, but if you want to try this challenge its probably
# easier to set up a VM emulating an intel machine anyway.

FROM debian:bookworm-slim

RUN dpkg --add-architecture i386 && \
    apt-get update && \
    apt-get install -y --no-install-recommends \
    libc6:i386 \
    lib32z1 \
    libncurses6:i386 \
    libstdc++6:i386 \
    socat=1.7.4.4-2 && \
    rm -rf /var/lib/apt/lists/*

COPY vuln flag.txt config.txt /home/ctf/
COPY food_dir/ /home/ctf/food_dir
RUN chmod +x /home/ctf/vuln && \
    useradd -ms /bin/bash ctf && \
    chown -R root:root /home/ctf &&\
    chown ctf:ctf /home/ctf/config.txt

USER ctf
WORKDIR /home/ctf

# Run the challenge using socat
EXPOSE 1358/tcp
CMD ["socat", "-dd", "TCP4-LISTEN:1358,fork,reuseaddr", "EXEC:/home/ctf/vuln,pty,echo=0,raw,iexten=0"]
