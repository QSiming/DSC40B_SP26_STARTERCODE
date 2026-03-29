#!/bin/env bash

# clone the autograder from github
# this file does not need to change between autograded problems

# the zip is extracted to this directory. the solution will be placed here, as well.
cd /autograder/source

apt-get install -y python3 python3-pip
pip3 install -r /autograder/source/requirements.txt
