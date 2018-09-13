package main

import "fmt"

//1  if语句
func if1(){
	var a int = 10 

	if a <20 {
		fmt.Printf("a litter then 20\n")
	}
	fmt.Printf("a的值为：%d\n",a)
}

//2  if else语句
func if2(){
	var a int = 10
	fmt.Println("if2 =====")
	if a < 20 {
		fmt.Printf("a litter then 20\n")
	} else {
		fmt.Printf("a  grester then 20\n")
	}
}

//3 swithch 语句
func if3(){
	//var grade string = "B"
    var score int = 60
	switch score {
	case 100:
		fmt.Println("特别优秀\n")
	case 90:
		fmt.Printf("很优秀\n")
	case 80:
		fmt.Printf("优秀\n")
	case 60,70:
		fmt.Printf("良好\n")
	fallthrough
	default:
		fmt.Printf("肯定不怎么样。\n")
	}
}
func main(){
	//if1()
	//if2()
	if3()
}
