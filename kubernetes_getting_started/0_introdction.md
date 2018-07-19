##  提及几个问题

#### kubernetes是干什么的？

#### 同类型的有哪些工具，优势是什么？

#### 有哪些基础知识？

#### 怎么用？






##  基本概念








###网络





Kubernetes集群内部存在三类IP，分别是：

Node IP：宿主机的IP地址
Pod IP：使用网络插件创建的IP（如flannel），使跨主机的Pod可以互通
Cluster IP：虚拟IP，通过iptables规则访问服务
