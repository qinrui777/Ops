

查看路由表
[root@node1 test]# ip route
default via 10.0.2.2 dev eth0 proto static metric 100
10.0.2.0/24 dev eth0 proto kernel scope link src 10.0.2.15 metric 100
172.17.8.0/24 dev eth1 proto kernel scope link src 172.17.8.101 metric 100
172.33.98.0/24 dev docker0 proto kernel scope link src 172.33.98.1

查看路由策略
[root@node1 test]# ip rule
0:	from all lookup local
32766:	from all lookup main
32767:	from all lookup default