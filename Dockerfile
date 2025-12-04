FROM jenkins/inbound-agent:latest

USER root

RUN apt-get update && apt-get install -y \
    git \
    build-essential \
    rpm \
    debhelper \
    devscripts \
    dos2unix \
    wget \
    docker.io \
    && rm -rf /var/lib/apt/lists/*

USER jenkins
