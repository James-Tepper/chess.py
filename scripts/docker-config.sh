#!/bin/bash

if [ -z "$1" ] || [ -z "$2" ] || [ -z "$3" ]
then
	echo "Provide a container name | image name | port number."
	exit 1
fi


export CONTAINER_NAME=$1
export IMAGE_NAME=$2
export PORT=$3


cd $(dirname "$0")

#Run
docker-compose up --build -d
