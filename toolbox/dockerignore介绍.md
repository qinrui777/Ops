- https://codefresh.io/docker-tutorial/not-ignore-dockerignore/
- https://yeasy.gitbooks.io/docker_practice/content/image/build.html

### build context
### The .dockerignore syntax
#### 不使用ignore的时候，也没有新加文件，构建test:v1
```sh
ip-10-209-20-202:ignore_test ruqin$ docker build -t test:v1 .
Sending build context to Docker daemon 2.048kB
Step 1/2 : FROM nginx
 ---> cd5239a0906a
Step 2/2 : RUN echo '<h1>Hello, Docker!</h1>' > /usr/share/nginx/html/index.html
 ---> Using cache
 ---> e12904fe5317
Successfully built e12904fe5317
Successfully tagged test:v1
```

#### 不使用ignore的时候，新加一个文件，构建test:v2

```sh
ip-10-209-20-202:ignore_test ruqin$ du -h *
4.0K	Dockerfile
372K	keynote-template1.key
ip-10-209-20-202:ignore_test ruqin$ docker build -t test:v2 .
Sending build context to Docker daemon 383kB
Step 1/2 : FROM nginx
 ---> cd5239a0906a
Step 2/2 : RUN echo '<h1>Hello, Docker!</h1>' > /usr/share/nginx/html/index.html
 ---> Using cache
 ---> e12904fe5317
Successfully built e12904fe5317
Successfully tagged test:v2
```
####  有了新文件之后，在ignore中忽略该文件，构建test:v3,可以看到  build context 又变小了
```sh
ip-10-209-20-202:ignore_test ruqin$ ls -al
total 760
drwxr-xr-x 5 ruqin staff 160 9 20 17:23 .
drwxr-xr-x 8 ruqin staff 256 9 20 17:17 ..
-rw-r--r-- 1 ruqin staff 25 9 20 17:23 .dockerignore
-rw-r--r-- 1 ruqin staff 81 9 20 17:18 Dockerfile
-rw-r--r--@ 1 ruqin staff 380395 9 20 17:21 keynote-template1.key
ip-10-209-20-202:ignore_test ruqin$ docker build -t test:v3 .
Sending build context to Docker daemon 3.072kB
Step 1/2 : FROM nginx
 ---> cd5239a0906a
Step 2/2 : RUN echo '<h1>Hello, Docker!</h1>' > /usr/share/nginx/html/index.html
 ---> Using cache
 ---> e12904fe5317
Successfully built e12904fe5317
Successfully tagged test:v3
```
