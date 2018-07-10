

#### 制作images

`cd /root/script/grafana_sync`

`docker build -t grafana_sync:v1.0 .`


#### 启动容器

`docker run  -e GRAFANA_TOKEN="changeMe" -e INTERVAL="600" -e LDAPPW="changeMe" --name grafana_sync -d grafana_sync:v1.0`