#!/bin/bash
app='jmrobinson/diceappv2'
docker build -t ${app} .
docker run -it -p 54321:5000 --name ${app} -v $PWD:/dice jmrobinson/diceappv2
