#!/bin/bash
for dir in */
do
    img=${dir%*/}   
    echo Build ${img} image as notebook:${img}
    docker image build -f ${img}/Dockerfile . -t notebook:${img} >> /dev/null 

done