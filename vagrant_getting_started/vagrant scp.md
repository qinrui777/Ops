## Using vagrant-scp.   
It adds a scp command to vagrant, so you can copy files to your VM like you would normally do with scp.


### Install via:

`vagrant plugin install vagrant-scp`


### Use it like so:

`vagrant scp <some_local_file_or_dir> [vm_name]:<somewhere_on_the_vm>`


###  example:  
```bash
$ vagrant scp README-cn.md node1:/home/README-cn.md
Warning: Permanently added '[127.0.0.1]:2222' (ECDSA) to the list of known hosts.
/etc/profile.d/lang.sh: line 19: warning: setlocale: LC_CTYPE: cannot change locale (UTF-8): No such file or directory
scp: /home/README-cn.md: Permission denied
CNruqin:kubernetes-vagrant-centos-cluster ruqin$ vagrant scp README-cn.md node1:/tmp/README-cn.md
Warning: Permanently added '[127.0.0.1]:2222' (ECDSA) to the list of known hosts.
/etc/profile.d/lang.sh: line 19: warning: setlocale: LC_CTYPE: cannot change locale (UTF-8): No such file or directory
README-cn.md                                                                                                100%   10KB   6.0MB/s   00:00
CNruqin:kubernetes-vagrant-centos-cluster ruqin$ vagrant ssh node1
Last login: Thu Aug  9 11:00:29 2018 from 10.0.2.2
-bash: warning: setlocale: LC_CTYPE: cannot change locale (UTF-8): No such file or directory
[vagrant@node1 ~]$ sudo su
[root@node1 vagrant]# cd /tmp/
[root@node1 tmp]# ls -l
total 20
-rw-r--r--  1 vagrant vagrant 10341 Aug  9 11:02 README-cn.md
-rwx--x--x. 1 vagrant vagrant  6282 Aug  8 12:00 vagrant-shell
```

>第一次scp 文件从host本机到vm 中的/home目录，发现目录权限不够，那就先scp到vm的 /tmp目录，后续在vm中再mv
