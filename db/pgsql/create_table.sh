## demo

read -d "" glogowner_itinerary << EOF
DROP TABLE IF EXISTS glogowner_itinerary;
create table glogowner_itinerary
(
 itinerary_xid      character varying(150)      ,
 itinerary_name     character varying(500)      ,
 hazmat_mode_gid    character varying(100)      ,
 itinerary_type     character varying(10)       ,
 attribute_number1  smallint                    ,
 attribute2         character varying(500)      ,
 attribute_date1    timestamp without time zone ,
 attribute_date2    timestamp without time zone ,
 update_date        timestamp without time zone
)
WITH (appendonly='true', compresslevel='5', orientation='column', compresstype=zlib)
DISTRIBUTED BY (itinerary_xid)
PARTITION BY RANGE (attribute_date1)
(
default partition default_p WITH (appendonly='true', compresslevel='5', orientation='column', compresstype=zlib),
partition pn start ('2019-01-01 00:00:00'::timestamp without time zone) end ('2031-01-01 00:00:00'::timestamp without time zone) every ('1 day'::interval)
WITH (appendonly='true', compresslevel='5', orientation='column', compresstype=zlib)
);
comment on column glogowner_itinerary.itinerary_xid is 'x';
comment on column glogowner_itinerary.itinerary_name is 'x';
comment on column glogowner_itinerary.hazmat_mode_gid is 'x';
comment on column glogowner_itinerary.itinerary_type is 'x(A--主干,M--备用,I--交派件,J--交件,P--派件,H--航空路由)';
comment on column glogowner_itinerary.attribute_number1 is 'x';
comment on column glogowner_itinerary.attribute2 is 'x';
comment on column glogowner_itinerary.attribute_date1 is '生效时间';
comment on column glogowner_itinerary.attribute_date2 is '失效时间';
comment on column glogowner_itinerary.update_date is '更新时间';
EOF
psql -d suanfa -h localhost -U gpadmin -p 5432 -c "$glogowner_itinerary"
