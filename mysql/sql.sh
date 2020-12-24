>> mysql reset password

# /etc/init.d/mysql stop
# mysqld_safe –skip-grant-tables &
# mysql -uroot -p

mysql>update mysql.user set password=password(‘mypassword’) where user=’root’;
mysql>flush privileges;
mysql>quit

grant all on *.* to root@'%' identified by 'your_password';



>> mysql load csv file

LOAD DATA LOCAL INFILE '/huangteng/ord.csv'
INTO TABLE shipment_ord_v1
FIELDS TERMINATED BY ',' ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 LINES
(pickup_date,waybill_number,originating_outlet,originating_distribution,handover_datetime, destination_outlet,destination_distribution,packages_weight,maximum_weight);
# SET handover_datetime = STR_TO_DATE(@handover_datetime, '%Y/%m/%d %H:%i%M');

INSERT INTO data (pickup_date,waybill_number,originating_outlet,originating_distribution,handover_datetime, destination_outlet,destination_distribution,packages_weight,maximum_weight)
SELECT  STR_TO_DATE(pickup_date, '%Y-%m-%d'),
        waybill_number,
        originating_outlet,
        originating_distribution,
        STR_TO_DATE(handover_datetime, '%Y-%m-%d %H:%i:%S'),
        destination_outlet,
        destination_distribution,
        packages_weight,
        maximum_weight
FROM  shipment_ord_v1;
