FROM ubuntu:20.04

# Set default values for environment variables
ARG PIPVERSION=23.0.1

# install python3.8
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    python3.8 \


    python3-pip \
    && rm -rf /var/lib/apt/lists/*

# # set up python environment. Default python is 3.6.9 -> upgrade to 3.8
# RUN update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.8 1
# RUN update-alternatives --config python3

WORKDIR /godeye

# Install necessary packages
RUN python3 -m pip install --no-cache-dir --upgrade pip==$PIPVERSION
COPY . /godeye 

# Install godeye core
RUN pip install --no-cache-dir -e .



