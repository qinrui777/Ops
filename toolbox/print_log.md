时间需要打印时间


所有可以每次调用一个函数，如下：

```bash
#!/bin/bash

log (){
    echo "*** `date +'%F %T'` $1 ***"
}

log "Start."
#your bash code


log "done."
```


显示如下：

```bash
➜  sh +x print_log.sh
*** 2019-06-21 10:37:06 Start. ***
*** 2019-06-21 10:37:06 done. ***
```
