package main

import "fmt"

var a int = 20

func main() {
	var a int = 10
	var b int = 20
	var c int = 0

	fmt.Println("main函数种的a = %d",a)
	fmt.Println("main函数种的c = %d",c)
	c =sum(a, b)
	fmt.Println("main函数种的c = %d",c)
	
}

func sum(a, b int) int {
	fmt.Println("sum函数种的a = %d",a)
	fmt.Println("sum函数种的b = %d",b)

	return a + b
}