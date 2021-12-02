#!/bin/bash

# 查询表结构
select COLUMN_NAME from information_schema.COLUMNS where table_name = "  ";


# 复制表结构
# create table addr_simulation (like addr_real INCLUDING DEFAULTS INCLUDING CONSTRAINTS INCLUDING INDEXES);
NOTICE:  table doesn't have 'DISTRIBUTED BY' clause, defaulting to distribution columns from LIKE table
CREATE TABLE

https://blog.csdn.net/wlwlwlwl015/article/details/52493197


# 新增字段
alter table i1_import_raw add column receiverTownName text;
alter table i1_import_raw add column receiverDetailAddress text null;
alter table i1_import_raw add column receiverTownName text null;

alter table i1_import_raw drop column receiverDetailAddress;
alter table i1_import_raw drop column rnship;


# 注意事项:
首先添加默认值的字段,然后再给已经添加的字段添加默认值, 速度较快.
alter table i1_import_raw add column receiverTownName text;
alter table i1_import_raw add column receiverTownName set default 'value';

# 日期转换
to_timestamp(substring(batch from 3),'yyyyMMddhh24miss')
psql -d  develop   -h  localhost   -U gpadmin  -p 5432  -c "insert into i1_order select to_timestamp(substring(batch from 3),'yyyyMMddhh24miss') as batch_time,* from i1_import_raw;"