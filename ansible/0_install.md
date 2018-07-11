## 搭建demo 环境

### 利用 vagrant+virtualbox


`vagrant up`


`cat  Vagrantfile`

```
Vagrant.configure("2") do |config|

    (1..2).each do |i|

        config.vm.define "node#{i}" do |node|

                # 设置虚拟机的Box
        node.vm.box = "ubuntu/trusty64"

                # 设置虚拟机的主机名
        node.vm.hostname="node#{i}"
                # 设置虚拟机的IP
        #node.vm.network "private_network", ip: "192.168.59.#{i}"
        node.vm.network "public_network", ip: "192.168.59.#{i}"

                # 设置主机与虚拟机的共享目录
        #node.vm.synced_folder "~/Desktop/share", "/home/vagrant/share"
                # VirtaulBox相关配置
        node.vm.provider "virtualbox" do |v|

                        # 设置虚拟机的名称
                v.name = "node#{i}"
                        # 设置虚拟机的内存大小
                v.memory = 1024
                        # 设置虚拟机的CPU个数
                v.cpus = 1
        end

                # 使用shell脚本进行软件安装和配置
        config.vm.provision :shell, inline: "echo C"

        end
    end
end
```


```
1) en0: Wi-Fi (AirPort)
2) p2p0
3) awdl0
4) en1: Thunderbolt 1
5) en2: Thunderbolt 2
6) bridge0
==> node2: When choosing an interface, it is usually the one that is
==> node2: being used to connect to the internet.
    node2: Which interface should the network bridge to? <6>
```


### demo 环境 安装和配置ansible

|Hostname|IP| role|Description|
|----|----|---|---|
|node1|192.168.59.1| 管理节点+被管理节点| none |
|node2|192.168.59.2| 被管理节点 | none |


在node1上
apt-get install ansible -y
```
cat /etc/ansible/hosts
[node1]
192.168.59.1

[node2]
192.168.59.2
```

ssh-keygen -t rsa 一路按回车即可

将公钥拷贝到被管理主机（node1,node2）上  

root@node1:~/.ssh# cat /root/.ssh/id_rsa.pub >> /root/.ssh/authorized_keys

#### 测试是否连通：  
```
root@node1:~/.ssh# ansible all -m ping
192.168.59.1 | success >> {
    "changed": false,
    "ping": "pong"
}

192.168.59.2 | success >> {
    "changed": false,
    "ping": "pong"
}
```
返回 success说明 成功，下面可以玩转了。



