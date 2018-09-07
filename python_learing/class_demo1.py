# -*- coding: utf-8 -*-
#!/usr/bin/env python

#----------------------------------------
#ref https://blog.csdn.net/wklken/article/details/6313265
#-----------------------------------------

class people:
    #定义基本属性
    name = ''
    age = ''
    gender = '' #man woman

    #定义构造方法（构造方法与其他普通方法不同的地方在于，当一个对象被创建后，会立即调用构造方法。）
    def __init__(self,n,a,g):
        self.name = n
        self.age = a
        self.gender = g
    

    def speak(self):
        print ("%s is speaking :I am %d years old" %(self.name,self.age))

zhangsan = people('zhangsan',21,'man')
zhangsan.speak()