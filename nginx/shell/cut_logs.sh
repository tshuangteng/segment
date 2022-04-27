#!/bin/sh
LANG=en_US.UTF-8

### 日志设置
log_path=/usr/src/log
log_file=$log_path/cut_logs.log

[ ! -d $log_path ] && mkdir -p $log_path
exec > $log_file 2>&1

### 日志按天切割
yest=$(date "+%Y%m%d")
i=1
while [ $i -le 2 ]; do
  now=$(date "+%Y%m%d")
  if [ $yest != $now ];then
      log_path=/usr/local/openresty/nginx/logs/access.log
      day_log_path=/usr/local/openresty/nginx/logs/access_$yest.log
      cp $log_path $day_log_path && echo "" > $log_path
      yest=now
  fi
  sleep 300
done