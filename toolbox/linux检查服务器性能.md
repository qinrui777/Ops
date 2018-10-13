概览：  
 - uptime  --------> load averages
 - top        -------> check overview
 - dmesg -T   | tail  ----->kernel errors
 - vmstat  -------->   overall stats by time
 - iostat   --------->  disk IO
 - pidstat -------> process usage
 - free   ----------> memery usage
 - sar   ----------> 




---

### iostat
功能：报告CPU利用率和磁盘I/O
用法: iostat [ 选项 ] [ <时间间隔> [ <次数> ] ]  
常用选项：
-c  显示CPU使用率  
-d  只显示磁盘使用率    
-k  单位KB/s代替Block/s  
-m  单位MB/s代替Block/s  
-N   显示所有映射设备名字  
-t  打印报告时间  
-x  显示扩展统计信息  


---
### vmstat 
功能：报告虚拟内存、swap、io、上下文和CPU统计信息。  
分析了这些文件：  
/proc/meminfo  
/proc/stat  
/proc/*/stat  
常用选项：  
-a  打印活跃和不活跃的内存页  
-d  打印硬盘统计信息  
-D  打印硬盘表  
-p  打印硬盘分区统计信息  
-s  打印虚拟内存表  
-m  打印内存分配（slab）信息  
-t  添加时间戳到输出  
-S  显示单位，默认k、KB、m、M，大写是*1024  


---



---


