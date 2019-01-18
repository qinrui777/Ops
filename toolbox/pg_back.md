### postgres 的数据库备份

#### 脚本如下

```bash
#!/bin/bash

date=`date "+%Y%m%d"`

dbNameArray=(
app1service
app2ervice
app3service
)

mkdir /apps/postgres_data_backup/${date}

for i in ${dbNameArray[@]};do
    echo "Backing up database ${i} for date ${date} ...."
    pg_dump -U postgres $i > /apps/postgres_data_backup/${date}/"${i}_${date}".sql
done
echo "****** Congratulations，well done !!!******"
```

#### 定时任务
```bash
# crontab -l
0 2 * * * /root/script/backup_ccp_db.sh >> /root/script/log.backup_pg_db
```
