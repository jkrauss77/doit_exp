FROM ubuntu:20.04

RUN apt-get update
RUN apt-get install -y -q python3-doit=0.31.1-3.2ubuntu1 python3 clang