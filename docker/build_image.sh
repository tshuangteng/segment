tag=$(date +%Y%m%d)-$(git rev-parse --short HEAD)

docker build -t 10.131.9.15:5000/python/xxxxxx:v$tag .

