###  docker ps 

`$ docker ps --help`

```
Usage:	docker ps [OPTIONS]

List containers

Options:
  -a, --all             Show all containers (default shows just running)
  -f, --filter filter   Filter output based on conditions provided
      --format string   Pretty-print containers using a Go template
  -n, --last int        Show n last created containers (includes all states) (default -1)
  -l, --latest          Show the latest created container (includes all states)
      --no-trunc        Don't truncate output
  -q, --quiet           Only display numeric IDs
  -s, --size            Display total file sizes
 ```
 
  #####  常用命令
  docker ps                 //查看正在运行的  
  docker ps -a             //查看所有的  
  docker ps -a -q         //只显示container id   
  
  docker ps --format='{{.Names}}'
  
查看退出状态的容器，并打印容器名  
`sh-4.2# docker ps -f status=exited --format="{{.Names}}"`

只列出镜像的id以及仓库名称：  
`sh-4.2# docker images --format "{{.ID}}: {{.Repository}}"`


只列出容器的相关id,image,status和name      
```
sh-4.2# docker ps --format "{{.ID}}: {{.Image}} : {{.Status}} : {{.Names}}"
66b60b72f00e: centos : Up 7 days : pensive_poincare
```
或者自己重新定义列,就和原生差不多:    
`sh-4.2# docker ps --format "table {{.ID}}\t{{.Image}}\t{{.Status}}\t{{.Names}}"`

### docker inspect 

定制显示docker列:

docker inspect --format='{{.State.Pid}}{{.Name}}' `docker ps -a -q`

显示则是 pid 与容器名称

对应个格式为 一级属性{{.属性}} 二级属性 {{.属性.属性}} 三级属性 {{.属性.属性.属性}}


### docker system

 `docker system df`

###  Docker 增强模板及函数

参考：
https://yq.aliyun.com/articles/230067
https://yq.aliyun.com/articles/272173
