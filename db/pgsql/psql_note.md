```shell
## 查看表大小
select relname, pg_size_pretty(pg_relation_size(relid)) from pg_stat_user_tables where schemaname='public' order by pg_relation_size(relid) desc;

## 查询表结构
select COLUMN_NAME from information_schema.COLUMNS where table_name = '';

## 从csv文件导入库
psql -d develop -h localhost -U gpadmin -p 5432 -c "\copy test_data_uniq_$DAY to '/gpdata/$DAY/gp_export_tmp.csv' with csv header delimiter ','";

## 导出csv文件
copy (select * from tb_scan limit 1) to '/gpdata/20220315/tmp/tb_scan.csv' with csv header delimiter ',';


## 分区表信息查看
select * from pg_partition_columns where tablename='tb_scan';
select * from pg_partition_columns where tablename='tu_doc_info';

select * from pg_partitions where tablename='tb_scan';
select * from pg_partitions where tablename='tu_doc_info';


## 查询主表及其分区表
# \dt* tb_scan*
suanfa=# \dt+ tb_scan*
                                         List of relations
 Schema |          Name           | Type  |  Owner  |       Storage        |  Size   | Description 
--------+-------------------------+-------+---------+----------------------+---------+-------------
 public | tb_scan                 | table | gpadmin | append only columnar | 1600 kB | 扫描信息
 public | tb_scan_1_prt_defp0     | table | gpadmin | append only columnar | 1600 kB | 
 public | tb_scan_1_prt_p20201201 | table | gpadmin | append only columnar | 1600 kB | 
 public | tb_scan_1_prt_p20201202 | table | gpadmin | append only columnar | 1600 kB | 
 public | tb_scan_1_prt_p20201203 | table | gpadmin | append only columnar | 1600 kB | 
 public | tb_scan_1_prt_p20201204 | table | gpadmin | heap                 | 800 kB  | 
 public | tb_scan_1_prt_p20201205 | table | gpadmin | heap                 | 800 kB  | 
(7 rows)

## 删除分区表
suanfa=# alter table "tb_scan" drop partition if exists "p20201204";
ALTER TABLE
suanfa=# alter table "tb_scan" drop partition if exists "p20201205";
ALTER TABLE

alter table tb_scan add partition p20220322 start (timestamp without time zone '2022-03-22 00:00:00') inclusive end (timestamp without time zone '2022-03-23 00:00:00') exclusive WITH (appendonly='true', compresslevel='5', orientation='column', compresstype=zlib);
alter table tu_doc_info add partition p20200601 start (timestamp without time zone '2020-06-01 00:00:00') inclusive end (timestamp without time zone '2020-06-02 00:00:00') exclusive WITH (appendonly='true', compresslevel='5', orientation='column', compresstype=zlib);


suanfa=# alter table tb_scan add partition p20201204 start (timestamp without time zone '2020-12-04 00:00:00') inclusive end (timestamp without time zone '2020-12-05 00:00:00') exclusive WITH (appendonly='true', compresslevel='5', orientation='column', compresstype=zlib);
NOTICE:  CREATE TABLE will create partition "tb_scan_1_prt_p20201204" for table "tb_scan"
ALTER TABLE

suanfa=# alter table tb_scan add partition p20201205 start ('2020-12-05 00:00:00'::timestamp without time zone) inclusive end ('2020-12-06 00:00:00'::timestamp without time zone) exclusive WITH (appendonly='true', compresslevel='5', orientation='column', compresstype=zlib);
NOTICE:  CREATE TABLE will create partition "tb_scan_1_prt_p20201205" for table "tb_scan"
ALTER TABLE


## Error
#CREATE TABLE p20201206 PARTITION OF tb_scan FOR VALUES FROM ('2020-12-06 00:00:00'::timestamp without time zone) TO ('2020-12-07 00:00:00'::timestamp without time zone);
#CREATE TABLE p20220322 PARTITION OF tb_scan FOR VALUES FROM ('2022-03-22 00:00:00') TO ('2022-03-23 00:00:^C')
```