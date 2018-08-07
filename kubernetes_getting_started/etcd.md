etcd 简介 https://yq.aliyun.com/articles/11035


etcd概念词汇表 
Raft：etcd所采用的保证分布式系统强一致性的算法。
Node：一个Raft状态机实例。
Member： 一个etcd实例。它管理着一个Node，并且可以为客户端请求提供服务。
Cluster：由多个Member构成可以协同工作的etcd集群。
Peer：对同一个etcd集群中另外一个Member的称呼。
Client： 向etcd集群发送HTTP请求的客户端。
WAL：预写式日志，etcd用于持久化存储的日志格式。
snapshot：etcd防止WAL文件过多而设置的快照，存储etcd数据状态。
Proxy：etcd的一种模式，为etcd集群提供反向代理服务。
Leader：Raft算法中通过竞选而产生的处理所有数据提交的节点。
Follower：竞选失败的节点作为Raft中的从属节点，为算法提供强一致性保证。
Candidate：当Follower超过一定时间接收不到Leader的心跳时转变为Candidate开始竞选。
Term：某个节点成为Leader到下一次竞选时间，称为一个Term。
Index：数据项编号。Raft中通过Term和Index来定位数据。


etcd 集群管理维护 http://www.ttlsa.com/fbs/etcd-cluster-manage/


```
export ETCDCTL_CA_FILE=/etc/kubernetes/ssl/ca.pem
export ETCDCTL_CERT_FILE=/etc/kubernetes/ssl/kubernetes.pem
export ETCDCTL_KEY_FILE=/etc/kubernetes/ssl/kubernetes-key.pem
```

```
etcdctl --endpoint "https://10.200.64.166:2379,https://10.200.64.243:2379,https://10.200.64.182:2379,https://10.200.64.242:2379,https://10.200.64.177:2379" member list
```

```
etcdctl --endpoint "https://10.200.64.166:2379,https://10.200.64.243:2379,https://10.200.64.182:2379,https://10.200.64.242:2379,https://10.200.64.177:2379" cluster-health
```
