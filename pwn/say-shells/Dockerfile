# (C) 2025 Jordan 'Starnsworth' Hawkes for Pecan+ CTF2025
# Starns@starnsworth.com

# SayShells! Vulnerable Web App Container v1.04

### Stage 1: Build requirements
FROM python:3.9-slim AS builder

ENV DEBIAN_FRONTEND=noninteractive

# Install dependencies
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        build-essential \
        gcc \
        make \
        perl \
        unzip \
        wget

RUN wget --progress=dot:mega https://backpan.perl.org/authors/id/E/EX/EXIFTOOL/Image-ExifTool-12.16.tar.gz && \
    tar xzf Image-ExifTool-12.16.tar.gz
WORKDIR /Image-ExifTool-12.16
RUN perl Makefile.PL && \
    make && \
    make install



# Set up app directory
WORKDIR /app
COPY templates/ /app/templates
COPY requirements.txt /app
COPY VulnExifWebApp.py /app
COPY flag.txt /

#install pyton dependencies.
RUN pip install --no-cache-dir -r requirements.txt

#add non-privlidged user and protect flag.
RUN useradd -m user && \
    chown root:root /flag.txt && chmod 444 /flag.txt && \
    passwd -l user && \
    mkdir -p /app/static /app/uploads && \
    chown -R user:user /app

    #switch to non-privlidged user.
USER user


#expose port
EXPOSE 5000
CMD ["python", "VulnExifWebApp.py"]
