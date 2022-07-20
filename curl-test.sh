#!/bin/bash

name=$RANDOM | md5sum | cut -c1-10;

curl --request POST http://localhost:5000/api/timeline_post -d 'name=${name}&email=c.o@g.com&content=test2'
echo "SE AGREGO"
curl http://localhost:5000/api/timeline_post
echo "VE"
curl --request DELETE http://localhost:5000/api/timeline_post -d 'name=${name}'
echo "SE ELIMINO"
curl http://localhost:5000/api/timeline_post
echo "VE"
