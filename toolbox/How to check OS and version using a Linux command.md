## Kernel Version

`uname -a`
`lsb_release -a`

## Distribution Information
cat /proc/version

### Debain . 
`cat /etc/*_version`

### Redhat . 
`cat /etc/redhat-release`  
`cat /etc/*-release`


 `cat /proc/version`  
However, use of /proc for things other than processes is now eschewed, so maybe it'll disappear someday.


### other tools . 
 **whatami** 

```sh
$ wget https://raw.githubusercontent.com/open-mpi/mtt/master/client/whatami/whatami && chmod a+x whatami
Resolving raw.githubusercontent.com... 151.101.116.133
Connecting to raw.githubusercontent.com|151.101.116.133|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 24434 (24K) [text/plain]
Saving to: 'whatami'

whatami                                           100%[============================================================================================================>]  23.86K  --.-KB/s    in 0.02s   

2018-08-15 18:54:42 (1.49 MB/s) - 'whatami' saved [24434/24434]

$ ./whatami
darwin-macosx_10.11-x86_64
```
