#!/bin/bash

# Update and upgrade the system
sudo apt-get update
sudo apt-get upgrade -y

# Install Python 3 and pip
sudo apt-get install -y python3
sudo apt-get install -y python3-pip

# Upgrade pip
pip3 install --upgrade pip

# Install PyQt5
pip3 install PyQt5
