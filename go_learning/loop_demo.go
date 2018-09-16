package main

import "fmt"

func main() {
	fmt.Printf("test for loop\n")
	var a int = 10

	LOOPxx: for a < 20{
		if a == 13 {
			a = a+1
			goto LOOPxx
		}
		fmt.Printf("a的值为：\n",a)
		a++
	}
}