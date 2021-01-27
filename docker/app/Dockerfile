FROM python:3.7

ARG WORKDIR=/usr/src/ht_web
COPY ./ $WORKDIR

# python env
ENV PYTHONPATH $WORKDIR
# necessary for set timezone
ENV LC_ALL C.UTF-8
ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update \
    # for netstat and ab command etc.
    && apt-get install -y cron vim wget net-tools apache2-utils \
    # for mysql
    python3-dev default-libmysqlclient-dev build-essential \
    # for chromium
    gconf-service libasound2 libatk1.0-0 libc6 libcairo2 libcups2 \
    libdbus-1-3 libexpat1 libfontconfig1 libgcc1 libgconf-2-4 libgdk-pixbuf2.0-0 libglib2.0-0 \
    libgtk-3-0 libnspr4 libpango-1.0-0 libpangocairo-1.0-0 libstdc++6 libx11-6 libx11-xcb1 libxcb1 libxcomposite1 \
    libxcursor1 libxdamage1 libxext6 libxfixes3 libxi6 libxrandr2 libxrender1 libxss1 libxtst6 ca-certificates fonts-liberation \
    libappindicator1 libnss3 lsb-release xdg-utils \
    && apt-get update \
    # for nginx
    && apt-get -y install --no-install-recommends wget gnupg ca-certificates \
    && wget -O - https://openresty.org/package/pubkey.gpg | apt-key add - \
    && apt-get -y install --no-install-recommends software-properties-common \
    && add-apt-repository -y "deb http://openresty.org/package/debian $(lsb_release -sc) openresty" \
    # && echo "deb http://openresty.org/package/ubuntu xenial main" > /etc/apt/sources.list.d/openresty.list \  for ubuntu 16
    && apt-get update \
    && apt-get -y install --no-install-recommends openresty \
    # for python
    && pip3 install --upgrade pip setuptools \
    && if [ ! -e /usr/bin/pip ]; then ln -s pip3 /usr/bin/pip ; fi \
    && if [ ! -e /usr/bin/python ]; then ln -s python3 /usr/bin/python ; fi \
    && pip3 install --no-cache-dir -r $WORKDIR/requirements.txt \
    # set timezone
    && cp /usr/share/zoneinfo/Asia/Shanghai /etc/localtime \
    && chmod +x $WORKDIR/start.sh \
    && rm -rf /var/log/apt/* \
    && rm -rf /var/cache/* \
    && rm -rf /root/.cache \
    && rm -rf /var/lib/apt/lists/* \
    && apt-get clean

ENV HOME $WORKDIR

# Notice

# 1
# "cp /usr/share/zoneinfo/Asia/Shanghai /etc/localtime" better than " ENV TZ='Asia/Shanghai' "
# because crontab server read Time from "/etc/localtime"

# 2
# don't set "ENV HOME" at file begin
# because install some service will rely on home path. It leads to the failure of starting for the service