### 初始化demo环境

| hostname |       ip     | role   |
| ---------|  ------------| -------|
|   node1  | 192.168.59.1 | 管理机  | 
|   node2  | 192.168.59.2 | 被管理机| 

`vagrant up`


安装基础命令
`yum install -y vim git net-tools`


安装ansible（ node1上即可）
`yum install -y ansible`



```bash
➜  vagrant-cluster vagrant ssh node1
Last login: Thu Oct 25 02:00:16 2018 from 10.0.2.2
[vagrant@node1 ~]$ sudo su -
Last login: 四 10月 25 02:00:19 UTC 2018 on pts/0
yum install -y ansible`
```
