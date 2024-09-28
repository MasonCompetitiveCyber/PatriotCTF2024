#!/bin/bash
docker rm -f secret_door
docker build --tag=secret_door .
docker run -dp 1337:1337 --rm --name=secret_door secret_door
