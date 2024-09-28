#!/bin/bash
docker rm -f bdog_nom
docker build --tag=bdog_nom .
docker run -p 3000:3000 --rm --name=bdog_nom bdog_nom -d