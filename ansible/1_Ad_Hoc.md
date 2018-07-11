## Ansible Ad-Hoc 命令

### 格式
`ansible <pattern_goes_here[webservers, all, *]> -m <module_name> -a <arguments>`


### ping 命令
`# ansible all -m ping`
```
192.168.59.1 | success >> {
    "changed": false,
    "ping": "pong"
}

192.168.59.2 | success >> {
    "changed": false,
    "ping": "pong"
}
```

###  拷贝文件
拷贝文件/etc/host到远程主机node2，位置为/tmp/node1_file

`# ansible node2 -m copy -a "src=/home/vagrant/ansible_demo/node1_file dest=/tmp/node1_file"`

```
192.168.59.2 | success >> {
    "changed": true,
    "dest": "/tmp/node1_file",
    "gid": 0,
    "group": "root",
    "md5sum": "d41d8cd98f00b204e9800998ecf8427e",
    "mode": "0644",
    "owner": "root",
    "size": 0,
    "src": "/root/.ansible/tmp/ansible-tmp-1531303267.16-117647051071986/source",
    "state": "file",
    "uid": 0
}
```

### 查看远程主机的全部系统信息
`# ansible all -m setup`
```
192.168.59.1 | success >> {
    "ansible_facts": {
        "ansible_all_ipv4_addresses": [
            "10.0.2.15",
            "192.168.59.1"
        ],
        "ansible_all_ipv6_addresses": [
            "fe80::a00:27ff:fe21:da00",
            "fe80::a00:27ff:fe7a:4333"
        ],
        "ansible_architecture": "x86_64",
        "ansible_bios_date": "12/01/2006",
        "ansible_bios_version": "VirtualBox",
        "ansible_cmdline": {
            "BOOT_IMAGE": "/boot/vmlinuz-3.13.0-147-generic",
            "console": "ttyS0",
            "ro": true,
            "root": "UUID=d1702e77-b50e-46dd-82d2-d58c6dcaf53b"
        },
        "ansible_date_time": {
            "date": "2018-07-11",
            "day": "11",
            "epoch": "1531303410",
            "hour": "10",
            "iso8601": "2018-07-11T10:03:30Z",
            "iso8601_micro": "2018-07-11T10:03:30.668541Z",
            "minute": "03",
            "month": "07",
            "second": "30",
            "time": "10:03:30",
            ......省略3278行
```            
其他小例子：
`ansible  node1 -m setup -a "filter=ansible_hostname"`

`ansible  node1 -m setup -a "filter=ansible_all_ipv4_addresses"`
