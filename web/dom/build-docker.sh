#!/bin/bash
docker rm -f sauman
docker build -t sauman:firstone .
docker run -p 9090:9090 --rm --name sauman sauman:firstone
