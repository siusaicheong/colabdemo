#!/bin/bash
echo 'Hello. Loading the program'
wget -O /usr/local/share/jupyter/nbextensions/google.colab/example12345678.jpg https://upload.wikimedia.org/wikipedia/commons/thumb/5/51/Thomas_Cook_Dublin_protest.jpg/120px-Thomas_Cook_Dublin_protest.jpg
python start.py
start.InvokeButton('click me', start.do_something)
