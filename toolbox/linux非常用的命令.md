
## 介绍些linux 不太常用的命令
---


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

