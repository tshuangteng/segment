#!/bin/bash


# 复制表结构
# create table addr_simulation (like addr_real INCLUDING DEFAULTS INCLUDING CONSTRAINTS INCLUDING INDEXES );
NOTICE:  table doesn't have 'DISTRIBUTED BY' clause, defaulting to distribution columns from LIKE table
CREATE TABLE

https://blog.csdn.net/wlwlwlwl015/article/details/52493197


# 新增字段
alter table i1_import_raw add column receiverTownName text;
alter table i1_import_raw add column receiverTownName text null;
alter table i1_import_raw drop column receiverDetailAddress;

# 注意事项:
首先添加默认值的字段,然后再给已经添加的字段添加默认值, 速度较快.
alter table i1_import_raw add column receiverTownName text;
alter table i1_import_raw add column receiverTownName set default 'value';

