#!/bin/bash

image_name="py-piscine"
container_name="py-piscine"

if ! docker image ls | grep "$image_name"; then
	docker build -t "$image_name" .
fi

if ! docker container ls -a | grep "$container_name" ; then
	export IP=$(ifconfig en0 | grep inet | awk '$1=="inet" {print $2}')
	xhost +$IP
	docker run -d -it --rm -e DISPLAY=$IP:0 --name "$container_name" -v ./src:/src "$image_name"
fi

docker exec -it "$container_name" /bin/bash
