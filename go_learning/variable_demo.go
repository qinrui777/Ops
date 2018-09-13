package main

//http://www.runoob.com/go/go-variables.html


//变量声明
//第一种 指定变量类型，声明后若布赋值，使用默认值
var v_name v_type
v_name = value

//第二种，根据值自行判定变量类型


//第三种 省略var 使用 :=  其左侧的变量不应该是已经声明过的，否则会导致变异错误
v_name := value