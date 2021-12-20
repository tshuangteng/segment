# delete container
docker rm `docker ps -qf status=exited`
docker rm `docker ps -aq`

# delete images
docker rmi `docker -aq`

