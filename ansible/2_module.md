### 简介
模块(也被称为 “task plugins” 或 “library plugins”)是在 Ansible 中实际在执行的.它们就 是在每个 playbook 任务中被执行的.你也可以仅仅通过 ‘ansible’ 命令来运行它们.  

### 常用模块
- ping
- command
- copy
- service
- yum 
- apt

### 参数

```
-i 设备列表路径，可以指定一些动态路径
-f 并发任务数
-private-key 私钥路径
-m 模块名称
-M 模块夹的路径
-a 参数
-k 登陆密码
-K sudo密码
-t 输出结果保存路径
-B 后台运行超时时间
-P 调查后台程序时间
-u 执行用户
-U sudo用户
-l 限制设备范围
-s 是此用户sudo无需输入密码
```

### 所有模块

官方文档：https://docs.ansible.com/ansible/latest/modules/modules_by_category.html

root@node1:/home/vagrant/ansible_demo# ansible-doc -l
acl                  Sets and retrieves file ACL information.
add_host             add a host (and alternatively a group) to the ansible-playbo
airbrake_deployment  Notify airbrake about app deployments
apt                  Manages apt-packages
apt_key              Add or remove an apt key
apt_repository       Add and remove APT repositores
arista_interface     Manage physical Ethernet interfaces
arista_l2interface   Manage layer 2 interfaces
arista_lag           Manage port channel (lag) interfaces
arista_vlan          Manage VLAN resources
assemble             Assembles a configuration file from fragments
assert               Fail with custom message
at                   Schedule the execution of a command or scripts via the at co
authorized_key       Adds or removes an SSH authorized key
......省略近200  
bigip_pool           Manages F5 BIG-IP LTM pools
bigip_pool_member    Manages F5 BIG-IP LTM pool members
boundary_meter       Manage boundary meters
bzr                  Deploy software (or files) from bzr branches
campfire             Send a message to Campfire

### 查看模块的具体使用
ansible-doc <apt>

```


示例：
ansible node2 -m apt -a "name=lrzsz state=latest"
ansible node2 -m apt -a "name=lrzsz state=absent"
