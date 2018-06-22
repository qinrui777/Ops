### 目的
仓库位于 **nexus** ，由于某些原因需要迁移到新的仓库 **harbor** 中, 由于数量较多，需要脚本完成

### 前提须知
迁移的操作大致为： **pull** -> **retag** -> **push** 

仓库需要登录后，才能 pull 、push , 登录后会生成一个文件 /root/.docker/config.json

### 仓库的接口
获取仓库 repositories
获取每个 repositories 下的 tag 


### 注意事项
镜像过多之后，记得删除 ，不然会挤爆本地机器的空间
