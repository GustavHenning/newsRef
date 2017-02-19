#!/bin/bash

#install goose
git clone https://github.com/grangier/python-goose.git
cd python-goose
sudo pip install -Ur requirements.txt
sudo python setup.py install
cd ..
rm -rf python-goose

#install pyteaser
sudo pip install -U pyteaser
echo "done"
