# -*- coding: utf-8 -*-
#!/usr/bin/env python 
import sys

#sys.argv[]是用来获取命令行参数的

###类型
#print type(sys.argv)
##长度
#print len(sys.argv)
##第一个参数
#print sys.argv[0]
##第二个参数
#print sys.argv[1]

def get_name():
    print "print name..."

def get_age():
    print "print age..."

if __name__== "__main__":
    print "===being==="
    get_name()
    if sys.argv[1].startswith('--'):
        option = sys.argv[1]
        print option
