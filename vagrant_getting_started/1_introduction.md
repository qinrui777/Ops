http://www.cnblogs.com/alexyang8/p/3380936.html

## 是什么？
Vagrant是一个简单易用的部署工具，用英文说应该是orchestration tool。它能帮助开发人员迅速的构建一个开发环境，帮助测试人员构建测试环境。




## 有什么用？
开发环境部署
作为开发人员可能会涉及到不同的开发语言和不同的包依赖，搭建开发环境总是一件很麻烦的事情，有些语言有强有力的项目构建工具支持，比如Java的Maven，而有些语言则没有这么方便的工具，比如Python。特别是随着时间的推移，开发环境也会变得很混乱。
Vagrant通过脚本文件的描述创建一个虚拟机实例，并通过shell脚本或puppet配置好开发环境，解决了开发环境的自动化搭建。同时，vagrant创建的开发环境也能被轻松的清理和共享，特别是对于一个团队，构建标准的开发环境将变得很轻松。
测试环境部署
对于测试环节中的集成测试，特别是分布式系统的集成测试，测试环境的搭建也是一个费时费力的工作。Vagrant支持多个实例的部署，可以在单机上创建多个虚拟机实例进行自动化的集成测试。如果单机的测试环境还不够大，也可以将这个工作交给AWS和OpenStack这样的云去完成。

## Vagrant的主要概念 
### Provider 
Provider指的是为Vagrant提供虚拟化支持的具体软件，比如vmware或virtual box。 
### Box 
Box代表虚拟机镜像。Vagrant根据Porvider的不同提供了很多的基础镜像（通过url从s3上获取），用户可以根据自己的需求使用vagrant package制作属于自己的box。
### Project 
一个目录和目录中的Vagrantfile就组成了vagrant的一个项目，项目下可以有子项目，子项目中的Vagrantfile配置将继承和重写父项目的配置。项目的虚拟机实例并不会存储在这个目录（存储在~/.vagrant.d/box下），所以可以通过git等版本管理工具来管理项目。
### Vagrantfile 
Vagrant的配置文件，使用Ruby的语法描述。里面定义了项目所使用的box，网络，共享目录，provision脚本等。当vagrant up命令运行时，将读取当前目录的Vagrantfile。
###  Provisioning 
Provisioning指的是虚拟机实例启动后，所需要完成的基础配置工作，比如说安装LAMP服务等。Vagrant支持使用shell，puppet，chef来完成provisioning工作。
###  Plugin 
Vagrant提供了插件机制，可以很好的扩展对宿主机OS, GuestOS，Provider，Provisioner的支持，比如vagrant的aws和openstack支持都是通过plugin来实现的。


## 如何使用？

安装Provider
我们使用VirtualBox作为虚拟化的Provider，下载并安装VirtualBox即可。https://www.virtualbox.org/wiki/Downloads

安装Vagrant
Vagrant提供了windows，mac，deb和rpm的安装包，下载最新版本1.3.5的安装即可。Ubuntu软件仓库的版本是1.0.1的，比较老了，在读取配置文件的时候可能会遇到问题，所以不建议直接从仓库安装。

http://downloads.vagrantup.com/


创建项目 
创建一个文件夹，并进入   

mkdir linux-dev  
cd linux-dev  
初始化项目  

vagrant init precise64 http://files.vagrantup.com/precise64.box  
运行玩命令后，我们应该会发现在当前目录下出现了Vagrantfile文件，内容如下：  


这个文件有详细的注释和说明，其中config.vm.box指定了所使用的box，如果该box不存在于本地，vagrant将会自动从config.vm.box_url处下载并添加到本地。

从名字可以看出这个box是一个ubuntu server 12.04 64位的virtual box镜像。  

配置provisioning脚本  
我们通常在安装完操作系统后希望能装一些软件或做一些配置，provisioning脚本正好能完成这个工作。比如完成操作系统安装后自动安装vim和git。

编辑Vagrantfile，添加一行
```
  # The url from where the 'config.vm.box' box will be fetched if it
  # doesn't already exist on the user's system.
  config.vm.box_url = "http://files.vagrantup.com/precise64.box"
  # 添加下面的这行
  config.vm.provision "shell", path: "provision.sh"  
```

这一行指定了provision使用shell脚本，shell脚本位于与Vagrantfile同目录下的provision.sh

创建provision.sh

`sudo apt-get install vim git -y`


启动实例
在linux-dev目录下运行vagrant up，vagran就会启动由该目录下Vagrantfile指定的虚拟机实例。

首先，vagrant会去本地查找box，如果没有就从远程下载（从s3上下载很慢，可以先用迅雷离线下载到本地，然后再通过vagrant box add命令来添加）；

然后，vagrant就会启动虚拟机，做一些网络配置，并将当前目录挂载到虚拟机的/vagrant下，使其能在虚拟机和物理机直接共享。

最后，vagrant会开始provisioning的过程，为虚拟机配置基础的软件(只在第一次启动时进行，以后可通过vagrant provision命令触发)。

SSH登陆
使用vagrant ssh命令可以登陆到虚拟机上，进行相应的操作，比如：
```
vagrant@precise64:~$ ls -lah /vagrant/
total 16K
drwxr-xr-x  1 vagrant vagrant  170 Oct 23 07:54 .
drwxr-xr-x 24 root    root    4.0K Oct 23 07:19 ..
-rw-r--r--  1 vagrant vagrant   32 Oct 23 07:54 provision.sh
drwxr-xr-x  1 vagrant vagrant  102 Oct 23 05:51 .vagrant
-rw-r--r--  1 vagrant vagrant 4.6K Oct 23 07:45 Vagrantfile
```


关闭实例
关闭实例可以使用三种方式vagrant suspending, vagrant halt, vagrant destroy。

- suspending，暂停虚拟机，保存虚拟机当前的状态（内存和磁盘均不释放），可以使用vagrant up命令恢复运行；
- halt，关机，虚拟机停止运行，但是虚拟机实例保留，不销毁，可以理解为是正常的关机；
- destroy，销毁虚拟机，虚拟机的实例被销毁;


> 相关资源
官网：http://www.vagrantup.com

文档: http://docs.vagrantup.com/v2/

Box：http://www.vagrantbox.es/

