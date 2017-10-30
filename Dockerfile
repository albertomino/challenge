FROM python:2.7
RUN apt-get update
RUN apt-get --assume-yes -y install libxml2-dev  libxslt1-dev python-dev zlib1g-dev
RUN DEBIAN_FRONTEND=noninteractive apt-get -y install tshark
RUN pip install lxml trollius logbook py pyshark click
WORKDIR /root
RUN git clone https://github.com/albertomino/challenge.git
WORKDIR /root/challenge
CMD ["mkdir","~/data_traffic"]
CMD ["python","capturing_v1.py","--nic","wlp2s0","--dump"]
