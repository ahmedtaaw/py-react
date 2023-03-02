docker-compose up
-then 
docker container ls
docker inspect [id for postgres]
Then take ipaddress and create by it database

-for python container
docker build . -t backend
docker run --name backend --rm -p 8000:8000 backend  
