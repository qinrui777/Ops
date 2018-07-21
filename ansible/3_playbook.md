### 作用

为了避免重复输入命令，Ansible提供脚本功能。Ansible脚本的名字叫Playbook，使用的是YAML的格式，文件以yml结尾。

注解：YAML和JSON类似，是一种表示数据的格式。


### playbook 基本要素/语法

 - hosts：为主机的IP，或者主机组名，或者关键字all
 - remote_user: 以哪个用户身份执行。
 - vars： 变量
 - tasks: playbook的核心，定义顺序执行的动作action。每个action调用一个ansbile module。
 
playbook常用到的YMAL格式：
　　1、文件的第一行应该以 "---" (三个连字符)开始，表明YMAL文件的开始。  
　　2、在同一行中，#之后的内容表示注释，类似于shell，python和ruby。  
　　3、YMAL中的列表元素以”-”开头然后紧跟着一个空格，后面为元素内容。  
　　4、同一个列表中的元素应该保持相同的缩进。否则会被当做错误处理。  
　　5、play中hosts，variables，roles，tasks等对象的表示方法都是键值中间以":"分隔表示，":"后面还要增加一个空格。  


### playbook脚本使用Module  
在playbook脚本中，tasks中的每一个action都是对module的一次调用。在每个action中：  
* 冒号前面是module的名字  
* 冒号后面是调用module的参数  
```
---
  tasks:
  - name: ensure apache is at the latest version
    yum: pkg=httpd state=latest
  - name: write the apache config file
    template: src=templates/httpd.conf.j2 dest=/etc/httpd/conf/httpd.conf
  - name: ensure apache is running
    service: name=httpd state=started
```

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



```
root@node1:/home/vagrant/ansible_demo/pb# cat vars.yml
---
- name: get vars
  hosts: node2
  user: root
  tasks:
  - name: get vars ipv4 ON methed 1
    shell: echo {{ ansible_eth1["ipv4"]["address"] }}
  - name: get vars ipv4 ON methed 2
    command: echo {{ ansible_eth1.ipv4.address }} >>/tmp/ip_method2
```


```
root@node1:/home/vagrant/ansible_demo/pb# cat when.yml
---
- name : test args when
  hosts: node2
  user: root
  tasks:
    - name: mkdir /tmp/debianDir when Debian
      command: mkdir - /tmp/debianDir
      when: ansible_os_family =="Debian"

    - name: mkdir /tmp/debianDir when centos
      command: mkdir -p /tmp/centosDir
      when: ansible_os_family =="CentOS"
```


### handlers
```
root@node1:/home/vagrant/ansible_demo/pb# cat install_apache.yml
---
- name: install apache
  hosts: node2
  remote_user: root
  tasks:
  - name: install apache on CentOS
    yum: name=httpd state=present
    when: ansible_os_family=="CentOS"
  - name: install apache on Debian
    apt: name=apache2 state=present
    when: ansible_os_family=="Debian"
    notify:
    - stop apache2

  handlers:
  - name: stop apache2
    service: name=apache2 state=stopped
 ```
 
 >  安装apache2后，会默认启动服务，所以此处 安装后触发停止apache2的服务的过程
 
> 提供json和yml互转的在线网站： http://www.json2yaml.com/
