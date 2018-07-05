```
$mkdir exit_demo
$cd exit_demo/
$ ls -l
$ echo kkk > file
```

```
CNruqin:exit_demo ruqin$ cat file
kkk
CNruqin:exit_demo ruqin$ echo $?
0
```
The command was successful. The file exists and there are no errors in reading the file or writing it to the terminal. The exit code is therefore 0.

```
CNruqin:exit_demo ruqin$ cat wrong_file
cat: wrong_file: No such file or directory
CNruqin:exit_demo ruqin$ echo $?
1
```
The exit code is 1 as the operation was not successful.
```
CNruqin:exit_demo ruqin$ catt file
-bash: catt: command not found
CNruqin:exit_demo ruqin$ echo $?
127
```


```
#!/bin/bash

cat file.txt 

if [ $? -eq 0 ]
then
  echo "The script ran ok"
  exit 0
else
  echo "The script failed" >&2
  exit 1
fi
```


What exit code should I use?
The Linux Documentation Project has a list of reserved codes that also offers advice on what code to use for specific scenarios. These are the standard error codes in Linux or UNIX.

1 - Catchall for general errors
2 - Misuse of shell builtins (according to Bash documentation)
126 - Command invoked cannot execute
127 - “command not found”
128 - Invalid argument to exit
128+n - Fatal error signal “n”
130 - Script terminated by Control-C
255\* - Exit status out of range

> 参考链接 https://shapeshed.com/unix-exit-codes/
