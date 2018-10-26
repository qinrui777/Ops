### tip 1 修改linux终端 命令行颜色

```sh
vim .bashrc
##将下面命令添加到最后
PS1="\[\e[37;40m\][\[\e[32;40m\]\u\[\e[37;40m\]@\h \[\e[36;40m\]\w\[\e[0m\]]\\$ "
source .bashrc
```

### tip 2 给服务器设置一个hostname的标签
- For centos 
```bash
vim /etc/bashrc 
##将下面命令添加到最后
USER_DEFINED_HOSTNAME=DD_WEB
PS1="(${USER_DEFINED_HOSTNAME})${PS1}"
```
效果如下：
`(DD_WEB)[root@node1 ~/Ops]#  `

- For suse
```bash
cat /etc/bash.bashrc.local
###XXXX
USER_DEFINED_HOSTNAME=DD_WEB
PS1="(${USER_DEFINED_HOSTNAME})${PS1}"
```

### tip 2 打印大字体

You can use following two programs to create colourful text banner:
- figlet - Display large characters made up of ordinary screen characters.
- toilet - Prints text using large characters made of smaller characters. It is similar in many ways to FIGlet with additional features such as Unicode handling, colour fonts, filters and various export formats.

```sh
yum intall -y epel-release
yum install -y figlet
```

让用户每次登录的时候打印 欢迎标语
```sh
echo "figlet w e l c o m e " >> ~/.bashrc
[root@node1 ~/Ops]# source ~/.bashrc
                   _
__      __   ___  | |   ___    ___    _ __ ___     ___
\ \ /\ / /  / _ \ | |  / __|  / _ \  | '_ ` _ \   / _ \
 \ V  V /  |  __/ | | | (__  | (_) | | | | | | | |  __/
  \_/\_/    \___| |_|  \___|  \___/  |_| |_| |_|  \___|
  ```