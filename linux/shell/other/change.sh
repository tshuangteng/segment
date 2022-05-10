#!/bin/bash

read -p "IP:" ip
read -p "HOSTNAME:" hostname

a3=`echo $ip |awk -F '.' '{print $3}'`
gateway=10.131.${a3}.1

cat > /etc/hosts << EOF
127.0.0.1	localhost
$ip	$hostname
EOF

cat > /etc/hostname << EOF
$hostname
EOF

cat > /etc/sysconfig/network-scripts/ifcfg-ens192 << EOF
DEVICE=ens192
NAME=ens192
TYPE=Ethernet
ONBOOT=yes
NM_CONTROLLED=no
BOOTPROTO=static
IPADDR=$ip
NETMASK=255.255.255.0
GATEWAY=$gateway
EOF

a4=`echo $ip |awk -F '.' '{print $4}'`
name=$a3$a4
nport=`cat /usr/local/nginx/conf/nginx.conf|grep listen|awk '{print $2}'|awk -F ';' '{print $1}'`

if [ $name -gt 65535 ];then
	sed -i "s/${nport}/${name:0:5}/g" /usr/local/nginx/conf/nginx.conf
else
	sed -i "s/${nport}/${name}/g" /usr/local/nginx/conf/nginx.conf
fi

cat > /etc/sysctl.conf << EOF
net.ipv4.ip_forward = 0
net.ipv4.conf.default.accept_source_route = 0
kernel.sysrq = 1
kernel.core_uses_pid = 1
net.ipv4.tcp_syncookies = 1
kernel.msgmnb = 65536
kernel.msgmax = 65536
kernel.shmmni = 4096
kernel.sem = 250 512000 100 2048
net.ipv4.tcp_tw_recycle=1
net.core.netdev_max_backlog=10000
vm.overcommit_memory=2
net.ipv4.conf.all.arp_filter = 1 
net.ipv4.ip_local_port_range=1025 65535
kernel.msgmni = 2048
net.ipv6.conf.all.disable_ipv6=1
net.ipv4.tcp_max_tw_buckets = 5000
net.ipv4.tcp_max_syn_backlog = 8192
net.ipv4.tcp_keepalive_time = 600
EOF

pagesize=`getconf PAGESIZE`
mem=`cat /proc/meminfo |grep MemTotal|awk '{print $2}'`
echo -e "kernel.shmmax = $(($mem * 1024 * 9 / 10))\nkernel.shmall = $(($mem * 1024 * 9 / 10 / $pagesize))\n" >> /etc/sysctl.conf