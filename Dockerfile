# docker build -t ubuntu1604py36
FROM ubuntu:16.04

RUN apt-get update
RUN apt-get install -y software-properties-common vim
RUN add-apt-repository ppa:jonathonf/python-3.5
RUN apt-get update

RUN apt-get install -y build-essential python3.5 python3.5-dev python3-pip python3.5-venv
RUN apt-get install -y git wget net-tools unzip


# update pip
RUN python3.5 -m pip install pip --upgrade
RUN python3.5 -m pip install wheel

RUN python3.5 -m pip install pyNaCl