#!/bin/bash
docker rm -f impersonate
docker build --tag=impersonate .
docker run -dp 9999:9999 --rm --name=impersonate impersonate