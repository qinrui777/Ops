# 利用  python SimpleHTTPServer 组合 ngrok下载本地文件到服务器上


step 1 :开启 http 
python -m SimpleHTTPServer 7777

step 2: 开启ngrok 

`cd /Users/ruqin/Downloads && ./ngrok http 7777`

可得到如下域名：
http://f66f25a0.ngrok.io


在服务器上访问该外网域名,即可下载本地文件
`wget  http://f66f25a0.ngrok.io/test.txt`


---
## SimpleHTTPServer


SimpleHTTPServer是Python 2自带的一个模块，是Python的Web服务器。它在Python 3已经合并到http.server模块中。


###  使用

1）进入待分享的目录   
2）执行命令  
`python -m SimpleHTTPServer <port>`     
    注意：不填端口号则默认使用8000端口。     
3）浏览器访问该主机的地址：
     http://IP:端口号/
  
  
## ngrok

ngrok 内网穿透利器

###  下载
去[官网](https://ngrok.com/download)下载


### 使用
`./ngrok http <port>`

