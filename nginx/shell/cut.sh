#!/bin/bash

# 设置日志文件路径和文件名
LOG_DIR="/usr/local/openresty/nginx/logs/"
LOG_FILE="access.log"

while true
do
  # 获取当前日期和三天前的日期
  CURRENT_DATE=$(date +%Y-%m-%d)
  THREE_DAYS_AGO=$(date -d "3 days ago" +%Y-%m-%d)

  # 设置新的日志文件名和路径
  NEW_LOG_FILE="$LOG_DIR/$LOG_FILE-$CURRENT_DATE"

  # 检查新日志文件是否存在，如果存在则退出脚本
  if [ -f "$NEW_LOG_FILE" ]; then
    echo "New log file already exists, exiting script"
    exit 1
  fi

  # 检查旧日志文件是否存在
  OLD_LOG_FILE="$LOG_DIR/$LOG_FILE-$THREE_DAYS_AGO"
  if [ -f "$OLD_LOG_FILE" ]; then
    # 如果存在，则删除
    rm "$OLD_LOG_FILE"
  fi

  # 将原始日志文件移动到新的日志文件中
  mv "$LOG_DIR/$LOG_FILE" "$NEW_LOG_FILE"

  # 创建一个新的空日志文件
  touch "$LOG_DIR/$LOG_FILE"

  # 等待3天
  sleep 259200
done
