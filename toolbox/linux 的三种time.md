### ON Time , Linux VS Windows 

在windows下一个文件有三种时间属性：

- 创建时间

- 修改时间

- 访问时间


相似的在Linux下一个文件也有三种时间属性：

（与windows不同的是linux没有创建时间，而多了个访问时间）

- 访问时间（access time 简写为atime）

- 修改时间（modify time 简写为mtime）

- 状态修改时间(change time 简写为ctime)


### atime:（access time）  
显示的是文件中的数据最后被访问的时间，比如系统的进程直接使用或通过一些命令和脚本间接使用。（执行一些可执行文件或脚本）

### mtime: （modify time）  
显示的是文件内容被修改的最后时间，比如用vi编辑时就会被改变。（也就是Block的内容）

### ctime: （change time）  
显示的是文件的权限、拥有者、所属的组、链接数发生改变时的时间。当然当内容改变时也会随之改变（即inode内容发生改变和Block内容发生改变时）


```
vim testFile
root@precise64:~# stat testFile
  File: `testFile'
  Size: 12        	Blocks: 8          IO Block: 4096   regular file
Device: fc00h/64512d	Inode: 131080      Links: 1
Access: (0644/-rw-r--r--)  Uid: (    0/    root)   Gid: (    0/    root)
Access: 2018-07-01 05:19:35.822162926 +0000
Modify: 2018-07-01 05:19:35.822162926 +0000
Change: 2018-07-01 05:19:35.826162727 +0000
 Birth: -
root@precise64:~# vim testFile
root@precise64:~# stat testFile
  File: `testFile'
  Size: 12        	Blocks: 8          IO Block: 4096   regular file
Device: fc00h/64512d	Inode: 131080      Links: 1
Access: (0644/-rw-r--r--)  Uid: (    0/    root)   Gid: (    0/    root)
Access: 2018-07-01 05:20:14.884662439 +0000
Modify: 2018-07-01 05:19:35.822162926 +0000
Change: 2018-07-01 05:19:35.826162727 +0000
```
