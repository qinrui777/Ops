[TOC]

## 介绍些linux 不太常用的命令


<<<<<<< HEAD
### tee

```sh
[root@node2 vagrant]# tee --help
Usage: tee [OPTION]... [FILE]...
Copy standard input to each FILE, and also to standard output.

  -a, --append              append to the given FILEs, do not overwrite
  -i, --ignore-interrupts   ignore interrupt signals
      --help     display this help and exit
      --version  output version information and exit
```

```sh
[root@node2 vagrant]# echo 123 | tee aaa
123
[root@node2 vagrant]# echo 456 | tee -a aaa
456
[root@node2 vagrant]# cat aaa
123
456
```
=======

>>>>>>> 8dd378db1700cccaef581271883c017b206f1275

### seq

```sh
[root@node2 vagrant]# seq 5 10 > number.txt
[root@node2 vagrant]# cat number.txt
5
6
7
8
9
10
[root@node1 tmp]# seq -s "+" 5
1+2+3+4+5
[root@node1 tmp]# seq -s "+" 5 10
5+6+7+8+9+10
[root@node1 tmp]# echo $(( $(seq -s "+" 5 10)))
45
```

### shuf

生成随机序列
-i 输出数字范围
-o 结果写入文件
```sh
[root@node1 tmp]# seq 6 | shuf
1
6
3
5
2
4
```

### join

```sh
[root@node2 vagrant]# join -t ':' -o 1.1 2.2 /etc/passwd /etc/shadow
root:$1$ObNmXc7z$GkScFTu0VSq3KUJsnPDzD.
bin:*
daemon:*
adm:*
lp:*
sync:*
shutdown:*
halt:*
mail:*
.....
dockerroot:!!
```
### rev
reversing the order of characters in every line
```sh
[root@node1 tmp]# cat rev-test.txt
123456
abcd
[root@node1 tmp]# cat rev-test.txt  | rev
654321
dcba
[root@node1 tmp]# echo "thanks no" | rev
on sknaht
[root@node1 tmp]#
```

### mkdir touch 
Create a continuous directory or file
```sh
root@node1 tmp]# touch NN{1..3}
[root@node1 tmp]# ls -l
...
-rw-r--r--. 1 root root  0 10月  2 12:15 NN1
-rw-r--r--. 1 root root  0 10月  2 12:15 NN2
-rw-r--r--. 1 root root  0 10月  2 12:15 NN3
[root@node1 tmp]# mkdir {100..105}
[root@node1 tmp]# ls -l
total 4
drwxr-xr-x. 2 root root  6 10月  2 12:12 100
drwxr-xr-x. 2 root root  6 10月  2 12:12 101
drwxr-xr-x. 2 root root  6 10月  2 12:12 102
drwxr-xr-x. 2 root root  6 10月  2 12:12 103
drwxr-xr-x. 2 root root  6 10月  2 12:12 104
drwxr-xr-x. 2 root root  6 10月  2 12:12 105
-rw-r--r--. 1 root root  0 10月  2 12:12 a
-rw-r--r--. 1 root root  0 10月  2 12:12 b
-rw-r--r--. 1 root root  0 10月  2 12:12 c
-rw-r--r--. 1 root root  0 10月  2 12:12 d
```

### rename
Rename files in batches
```sh
[root@node1 tmp]# ls -l
...
-rw-r--r--. 1 root root  0 10月  2 12:15 NN1
-rw-r--r--. 1 root root  0 10月  2 12:15 NN2
-rw-r--r--. 1 root root  0 10月  2 12:15 NN3
[root@node1 tmp]# rename NN NNM NN?
[root@node1 tmp]# ls -l
...
-rw-r--r--. 1 root root  0 10月  2 12:15 NNM1
-rw-r--r--. 1 root root  0 10月  2 12:15 NNM2
-rw-r--r--. 1 root root  0 10月  2 12:15 NNM3
```


### dirname

```sh
[root@node1 100]# dirname /tmp/100/test
/tmp/100
[root@node1 100]# dirname /tmp/100/
/tmp
```

### basename

-a 多参数
-s 删除后面的后缀

```sh
[root@node1 tmp]# basename /ttt/ccc/xxx
xxx
[root@node1 tmp]# basename -s .txt /ttt/ccc/xxx.txt
xxx
[root@node1 tmp]# basename -a /tt/11 tt/222
11
222
```

### tr
替换或删除字符
格式： tr [OPTION] ... SET1 [SET2]
常用选项：
-c 替换SET1中没有SET2的字符
-d 删除SET1中字符
-s 缩压SET1中重复的字符
-t 将SET1用SET2转换，默认

```sh
[root@node1 tmp]# echo aaabbbccccc | tr -s '[a-d]'
abc
[root@node1 tmp]# echo "aaabbcc" | tr '[a-z]' '[A-Z]'
AAABBCC
```