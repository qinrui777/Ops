#ref: https://zhuanlan.zhihu.com/p/29859954

name = "Steven"
age = 45
height = 1.832

#方式一：用str函数统一成字符串
print("Method 1:  His name is " + name + ",and he is " + str(age))

#方式二： 用字符串格式化, 在引号后面写“%(变量名或者数据，多个数据用括号，单个数据随意)
# 常见的几个格式化
# %d: 整数
# %f: 浮点数
# %s: 字符串
print("Method 2:  His name is %s, and he is %d, height is %.2f meters" % (name,age,height))

#方式三：用format函数（推荐）
print("Method 3:  His name is {} ,and he is {}, height is {:.2f} meters".format(name,age,height))

# output:
# ```bash
# ➜   python3 print_format.py
# Method 1:  His name is Steven,and he is 45
# Method 2:  His name is Steven, and he is 45, height is 1.83 meters
# Method 3:  His name is Steven ,and he is 45, height is 1.83 meters
# ```