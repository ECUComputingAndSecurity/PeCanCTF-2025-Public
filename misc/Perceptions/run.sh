#!/bin/bash

# Quick spin-up for testing
set -e

sudo docker build -t aurillium/perceptions-chal .
sudo docker run -p 43713:43713 -it --name perceptions-chal --rm aurillium/perceptions-chal

