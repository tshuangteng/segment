import MySQLdb

from constant import MYSQL_PASS, MYSQL_USER, MYSQL_DB, MYSQL_PORT, MYSQL_HOST, TEST_TABLE

db = MySQLdb.connect(host=MYSQL_HOST, port=MYSQL_PORT, database=MYSQL_DB, user=MYSQL_USER, password=MYSQL_PASS, charset='utf8mb4')

cursor = db.cursor()

# ############################## create table #######################################
# sql = f"""
# CREATE TABLE `{TEST_TABLE}` (
#   `id` bigint(64) NOT NULL AUTO_INCREMENT COMMENT '主键',
#   `type` tinyint(1) NOT NULL COMMENT '店铺类型',
#   `name` varchar(64) NOT NULL COMMENT '店铺名称',
#   `sid` bigint(64) NOT NULL COMMENT '店铺唯一编码',
#   `items` bigint(64) NOT NULL COMMENT '店铺所有商品编码',
#   `describe` float(20, 4) DEFAULT 0 COMMENT '店铺宝贝描述',
#   `service` float(20, 4) DEFAULT 0 COMMENT '店铺卖家服务',
#   `delivery` float(20, 4) DEFAULT 0 COMMENT '店铺物流服务',
#   `create_time` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
#   `update_time` datetime DEFAULT NULL ON UPDATE CURRENT_TIMESTAMP COMMENT '修改时间',
#   PRIMARY KEY (`id`) USING BTREE,
#   UNIQUE INDEX `uniq_inx_sid` (`sid`) USING BTREE COMMENT '店铺编码唯一索引',
#   INDEX `inx_type` (`type`) USING BTREE COMMENT '店铺类型索引',
#   INDEX `inx_describe` (`describe`) USING BTREE COMMENT '宝贝描述索引',
#   INDEX `inx_service` (`service`) USING BTREE COMMENT '卖家服务索引',
#   INDEX `inx_delivery` (`delivery`) USING BTREE COMMENT '店铺物流索引'
# ) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8mb4 COMMENT='店铺表';
# """
# cursor.execute(sql)

############################# columns ##################################
sql_par = f'select COLUMN_NAME from information_schema.COLUMNS where table_name = "{TEST_TABLE}"'
cursor.execute(sql_par)
columns = [column[0] for column in cursor.fetchall()]
print(columns)
############################ or #################################
cursor.execute(f"SHOW columns FROM {TEST_TABLE}")
columns = [column[0] for column in cursor.fetchall()]
print(columns)
############################# or ###############################
cursor.execute(f"desc {TEST_TABLE}")
columns = [column[0] for column in cursor.fetchall()]
print(columns)

cursor.execute('drop table testv2;')
cursor.close()
db.close()
