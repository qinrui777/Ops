role 使用

playbook 直接调用 task 问题 
playbook 是需要处理的事情，task 是执行细节，playbook并不关心细节   
playbook 直接调用task 使task无法复用  
playbook会越来越长，难维护  
将一个或多个task抽象成一个role，隐藏细节，供playbook调用   
role易于复用，可以从一个已知的文件结构中自动加载vars, tasks, handler。
部分文件结构：
```sh
roles/
    install/
        files/
        templates/
        tasks/
            main.yml  #应用 install 时，优先执行main.yml
        handlers/
        vars/
    deploy/
        files/
        templates/
        tasks/
            main.yml
        handlers/
        vars/
```
```
---
- hosts: webservers
  roles:
     - install
     - deploy
```

###  建议的结构
参考 https://blog.goquxiao.com/posts/2015/09/01/ansible-simple-tutorial/
```sh
├── inventory                        # 存放主机/分组配置  
│   └── production   
└── playbooks                          # 第一层存放不同的剧本  
    ├── playbook1.yml  
    ├── playbook2.yml   
    ├── playbook3.yml  
    ├── playbook4.yml 
    ├── roles                         # 不同的角色 
    └── common 
        │   ├── defaults 
        │   ├── handlers  
        │   ├── library 
        │   ├── meta 
        │   ├── tasks 
        │   │   ├── main.yml 
        │   │   ├── rsync.yml 
        │   │   └── selinux.yml 
        │   └── vars 
        └── monitor                    # 一个名字叫monitor的模块 
            ├── defatuls 
            ├── files                  # 待上线的binary 
            │   └── monitor 
            │       └── bin 
            │           └── monitor 
            ├── handlers               # binary或者conf更新之后，执行的操作 
            │   └── main.yml 
            ├── meta 
            ├── tasks                   # 上线步骤 
            │   └── main.yml
            ├── templates              # 待上线的conf 
            │   └── monitor 
            │       └── conf 
            │           └── conf.ini 
            └── vars 
```
