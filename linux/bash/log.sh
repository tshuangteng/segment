#!/bin/sh
LANG=en_US.UTF-8

tod=$(date "+%Y%m%d")
today=$(date "+%Y-%m-%d")
tomorrow=$(date "+%Y-%m-%d" -d "-1 day ago")

# 配置日志
log_path=/suanfa/log/$tod
log_file=$log_path/prd_cron.log

[ ! -d $log_path ] && mkdir -p $log_path
exec > $log_file 2>&1
