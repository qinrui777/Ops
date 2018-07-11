role 使用
playbook 直接调用 task 问题
playbook 是需要处理的事情，task 是执行细节，playbook并不关心细节
playbook 直接调用task 使task无法复用
playbook会越来越长，难维护
将一个或多个task抽象成一个role，隐藏细节，供playbook调用
role易于复用，可以从一个已知的文件结构中自动加载vars, tasks, handler。
部分文件结构：

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


---
- hosts: webservers
  roles:
     - install
     - deploy
