— 进程太多，不知道子进程、父进程的关系，像是一团乱麻吗？
— 试试用 **pstree** ，




pstree -p 一键便可以梳理出服务器上的所用进程和其关联的进程


ps -ef | grep gitlab  的结果一眼看过去不知所踪

pstree -p <PID>

