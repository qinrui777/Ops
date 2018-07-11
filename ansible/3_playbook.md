### 作用

为了避免重复输入命令，Ansible提供脚本功能。Ansible脚本的名字叫Playbook，使用的是YAML的格式，文件以yml结尾。

注解：YAML和JSON类似，是一种表示数据的格式。


### playbook 基本要素

 - hosts：为主机的IP，或者主机组名，或者关键字all
 - remote_user: 以哪个用户身份执行。
 - vars： 变量
 - tasks: playbook的核心，定义顺序执行的动作action。每个action调用一个ansbile module。




示例：
```
# cat playbook1.yml
---
- hosts: node2
  remote_user: root
  tasks:
  - name: install lrzsz
    apt: name=lrzsz state=latest
   
   
# ansible-playbook  playbook1.yml

PLAY [node2] ******************************************************************

GATHERING FACTS ***************************************************************
ok: [192.168.59.2]

TASK: [install lrzsz] *********************************************************
changed: [192.168.59.2]

PLAY RECAP ********************************************************************
192.168.59.2               : ok=2    changed=1    unreachable=0    failed=0
```

> 提供json和yml互转的在线网站： http://www.json2yaml.com/
