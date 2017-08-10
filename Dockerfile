FROM python:3

WORKDIR /usr/src/app

# Define Libsodium version
ENV LIBSODIUM_VERSION 1.0.12

# Install some tools: gcc build tools, unzip, etc
RUN \
    apt-get update && \
    apt-get -y upgrade && \
    apt-get -y install curl build-essential unzip locate

# Download and install libsodium
# https://download.libsodium.org/doc/

# Download & extract & make libsodium
# Move libsodium build
RUN \
    mkdir -p /tmpbuild/libsodium && \
    cd /tmpbuild/libsodium && \
    curl -L https://download.libsodium.org/libsodium/releases/libsodium-${LIBSODIUM_VERSION}.tar.gz -o libsodium-${LIBSODIUM_VERSION}.tar.gz && \
    tar xfvz libsodium-${LIBSODIUM_VERSION}.tar.gz && \
    cd /tmpbuild/libsodium/libsodium-${LIBSODIUM_VERSION}/ && \
    ./configure && \
    make && make check && \
    make install && \
    && ﻿ldconfig \
    mv src/libsodium /usr/local/ && \
    rm -Rf /tmpbuild/

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD [ "python", "./server.py" ]