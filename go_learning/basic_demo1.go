package main

import "fmt"
import "unsafe"

//func add(x int , y int) int{
//	return x + y 
//}

//func add(x,y int) int{
//	return x+y
//}


func swap_demo(x,y string)(string,string){
	return y,x
}

func split(sum int) (x,y int){
	x = sum*4/9
	y = sum -x
	return y,x
}

//var c,python,java bool


//var b,d int

const (
	Unkown = 0
	Female = 1
	Male = 2
)

const (
	a = iota
	b = iota
	c = iota
)
func main(){
	//fmt.Println(swap_demo("first","second"))
	//fmt.Println(split(17))
	//var i int
	//fmt.Println(i,c,python,java)
	//var a string = "aaaaa"
	//fmt.Println("hello gogo")
	//fmt.Println(a)


}