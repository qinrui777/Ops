
运维到最后，一项工作就是备份；不怕一万就怕万一

### 备份的对象？
重要配置文件、产出物、数据库的数据文件等


### 备份的频次？
一般来说一天一次，而且都是晚上凌晨的时候自动做

###  备份方式？
crontab 

###  备份的周期？
有的文件或文件夹每次备份出来都有上G 容量，所以不能一直都存着，会把磁盘撑爆的，于是就需要删除比较老的备份内容，一般来说 **一周**、**一个月**的数据足矣。

示例一：

####   step 1 ：写脚本
```
#!/bin/bash

####################################
#   Function: backup jenkins_data
#   Period :  every day
#   Crontab : 1:00 am
#
###################################

BACKUP_PATH="/backup/jenkins_backup"

Today=`date +%Y%m%d`

tar -zcPf  ${BACKUP_PATH}/$Today.tar  /data/jenkins-data

find ${BACKUP_PATH} -name "*.tar" -ctime +7 -type f -exec rm -f {} \;

echo "********* " $Today " task done**********"
```

####  step 2 ： 中添加crontab 
```
# jenkins data backup
00 1 * * * bash /root/script/backup_jenkins.sh >> /root/script/backup_jenkins.log
```

如需每次运行生成一个日志文件
```bash
/home/start_service.sh >> /home/start_service.log.`date -I`
```

日期的样式如下：
```bash
[root@node1 tmp]# echo `date -I`
2018-08-09

touch app_`date +%Y%m%d%H%M`.log  

```



当然还有其他工具和策略

```bash
-ctime -n    查找距现在 n*24H 内修改过的文件
-ctime n    查找距现在 n*24H 前, (n+1)*24H 内修改过的文件
-ctime +n    查找距现在 (n+1)*24H 前修改过的文件
```

保留策略(安最新的文件数量保留)：
```bash
#!/bin/sh
echo "删除指定目录下result-order开头的文件，保留最新的5个"
report_dir='/Users/Shared/Jenkins/Home/workspace/pro_env_order'
save_num=5
cd $report_dir
save_file=`ls -lrt | grep 'result-order' | tail -$save_num | awk '{print $NF}'`
ls | grep 'result-order' | grep -v "$save_file" | xargs rm -rf
```
