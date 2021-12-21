
# mysql
docker run -p 3399:3306 --hostname=mysql --name=mysql -e TZ=Asia/Shanghai -e MYSQL_ROOT_HOST=% -e MYSQL_ROOT_PASSWORD=Yjy98092616 -e MYSQL_DATABASE=huangteng -e MYSQL_USER=mysql -e MYSQL_PASSWORD=yjy98092616 -d mysql/mysql-server:5.7 --character-set-server=utf8mb4 --collation-server=utf8mb4_unicode_ci
# reference: https://dev.mysql.com/doc/mysql-installation-excerpt/5.7/en/docker-mysql-more-topics.html

# or mysql
docker run --hostname=mysql --name=mysql -p 3306:3306 -e MYSQL_ROOT_HOST=% -e MYSQL_ROOT_PASSWORD=root -e MYSQL_DATABASE=test -e MYSQL_USER=mysql -e MYSQL_PASSWORD=mysql -d mysql/mysql-server:5.7 --character-set-server=utf8mb4 --collation-server=utf8mb4_unicode_ci
echo "default-time-zone = '+08:00'" >> /etc/my.cnf


# redis
docker run -itd -p 6399:6379 --hostname redis --name redis redis:alpine redis-server --requirepass Yjy98092616 --appendonly yes


#