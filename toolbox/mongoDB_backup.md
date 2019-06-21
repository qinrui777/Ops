### mongo db的备份 （方法之一）



#### 1. backup(备份)
```bash
kubectl -n <NAMESPACE> exec -it <POD_NAME> -- mongodummp -h localhost -d <DB_NAME> --gzip --archive=/tmp/xxx`date +"%Y%m%d%H%M"`
```


#### 2. restore(恢复)

`docker run -d --name mongo-test mongo`

`docker cp /Users/ruqin/Desktop/temp/xxx_mongo_201906201800.gz mongo-test:/tmp/`


`mongorestore -d <DB_NAME> --gzip --archive=/tmp/xxx_mongo_201906201800.gz`