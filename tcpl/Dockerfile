########################################### ubuntu pure system #########################################################
FROM ubuntu:20.04

ARG WORKDIR=/root/c_code
COPY ./ $WORKDIR

# necessary for set timezone
ENV LC_ALL C.UTF-8
ENV DEBIAN_FRONTEND noninteractive

EXPOSE 22

RUN apt-get update \
    && apt-get install -y vim net-tools tzdata openssh-server \
    && cp /usr/share/zoneinfo/Asia/Shanghai /etc/localtime \
    && apt-get update \
    && chmod +x $WORKDIR/start.sh \
    && rm -rf /var/log/apt/* \
    && rm -rf /var/cache/* \
    && rm -rf /root/.cache \
    && rm -rf /var/lib/apt/lists/* \
    && apt-get clean

ENV HOME $WORKDIR
# docker run -itd --name c_code --hostname c_code -e LC_ALL="C.UTF-8" -e DEBIAN_FRONTEND="noninteractive" -v /c/users/ht/documents/c_code:/root/c_code ubuntu:18.04 /bin/bash


############################################ use ubuntu:20.04 dockerhub ################################################
# vim start.sh
cp /usr/share/zoneinfo/Asia/Shanghai /etc/localtime
export LC_ALL="C.UTF-8"
tail -f /etc/profile
# docker run -itd --name gcc8 --hostname gcc8  ubuntu:20.04 /bin/bash start.sh


########################################## others  #####################################################################
# Windows OS
# CMD admin

# docker network create --driver bridge --subnet 10.10.0.0/16  --gateway 10.10.0.1 cppnet
# route add 10.10.0.0 mask 255.255.0.0 10.0.75.2 -p
# docker run -itd --name cpp --hostname cpp --net cppnet  --ip 10.10.54.54 --privileged=true -e LC_ALL="C.UTF-8" -e DEBIAN_FRONTEND="noninteractive" -v /c/users/ht/documents/_mine:/root ubuntu:18.04 /bin/bash

# 注:放弃 宿主机是ping不通容器的.ssh也没有办法使用.


#################################################### use gcc:8 dockerhub ################################################

# docker run -itd --name gcc8 --hostname gcc8 -e LC_ALL="C.UTF-8" -e "TZ=Asia/Shanghai" gcc:8 bash
