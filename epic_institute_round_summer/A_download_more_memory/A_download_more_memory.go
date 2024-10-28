package main

import "fmt"

func main() {
	var t, n, k int
	fmt.Scan(&t)

	for ; t > 0; t-- {
		fmt.Scan(&n, &k)
		fmt.Println((n-1)*k + 1)
	}

}
