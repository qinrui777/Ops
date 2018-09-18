repeat is a builtin command in csh and tcsh.

说是有，但是找不到安装包，于是采用下面的折中办法

I can't find this command on Ubuntu. It doesn't seem to exist. I even find it very weird that the post on StackOverflow says it's a builtin command when I can't find it on Ubuntu.

Edit: Like Matt noted, it is a builtin csh command. The following are tips to do quite the same with bash.

If what you want is to repeat a command n times, you can do that with a loop though:

for i in {1..n}; do yourcommand; done
For example, to print 100 times "It works", use:

for i in {1..100}; do echo "It works"; done
If you want to have a repeat function, you could add something like this to your ~/.bashrc:
```sh
function repeat() { 
    local times="$1"; 
    shift; 
    local cmd="$@"; 

    for ((i = 1; i <= $times; i++ )); do 
       eval "$cmd"; 
    done 
 }
 ```
 Source your ~/.bashrc again with . ~/.bashrc and you can call it:
 ```sh
 root@test-node:/home/vagrant# repeat 2 date
Tue Sep 18 10:16:33 UTC 2018
Tue Sep 18 10:16:33 UTC 2018
```
