FROM nvidia/cuda:10.2-devel-ubuntu18.04

ARG WORKDIR=/usr/src/ocr
COPY ./ $WORKDIR

ENV PYTHONPATH $WORKDIR
ENV PYTHONIOENCODING utf-8
ENV workspace $WORKDIR
ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update \
    && apt-get install -y vim wget net-tools apache2-utils tzdata lsb-core python3-pip libgl1-mesa-glx \
    && cp /usr/share/zoneinfo/Asia/Shanghai /etc/localtime \
    && apt-get -y install --no-install-recommends gnupg ca-certificates \
    && wget -O - https://openresty.org/package/pubkey.gpg | apt-key add - \
    && echo "deb http://openresty.org/package/ubuntu $(lsb_release -sc) main" > /etc/apt/sources.list.d/openresty.list \
    && pip3 install --upgrade pip \
    && apt-get update \
    && apt-get -y install --no-install-recommends openresty \
    && pip3 install --no-cache-dir -r $workspace/requirements.txt\
    && chmod +x $workspace/start.sh \
    && rm -rf /var/log/apt/* \
    && rm -rf /var/cache/* \
    && rm -rf /root/.cache \
    && rm -rf /var/lib/apt/lists/* \
    && apt-get clean


# for nvidia docker container
# with python3.6 on ubuntu18.04 system
# python's code setting use ENV
