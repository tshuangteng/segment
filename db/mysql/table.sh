
# 导出表
mysqldump -h xx.xx.xx.xx -P 3407 -u $DBUSER -p$PASSWD --skip-lock-tables demo gs > /my/app/demo.sql
