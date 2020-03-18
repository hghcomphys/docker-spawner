#!/bin/bash
for dir in */ # loop over all directories in the current directory
do
    img=${dir%*/}   
    echo Build ${img} image as notebook:${img}
    docker image build -f ${img}/Dockerfile . -t notebook:${img} #>> /dev/null 
done
