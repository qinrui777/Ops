# -*- coding: utf-8 -*-
#!/usr/bin/env python 

import os 

my_dict = {'name':'server1','privateIpAddress': '172.20.1.196', 'provisioningState': 'Succeeded'}

##遍历key
for i in my_dict.keys():
    print i

##遍历valua
for j in my_dict.values():
    print j

##遍历item(key-value形式)
for t in my_dict.items():
    print t

print "遍历item(key-value形式)"
for i,j in my_dict.items():
    print i,j

print "判断key是否存在"
print my_dict.has_key('name')

