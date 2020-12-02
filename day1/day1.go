package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"strconv"
)

func check(e error) {
	if e != nil {
		panic(e)
	}
}

func main() {
	fmt.Println("Hello, World!")
	file, err := os.Open("input.data")

	if err != nil {
		log.Fatalf("failed opening file: %s", err)
	}

	scanner := bufio.NewScanner(file)
	scanner.Split(bufio.ScanLines)
	var txtlines []string

	for scanner.Scan() {
		txtlines = append(txtlines, scanner.Text())
	}

	file.Close()

	for _, i := range txtlines {
		one, _ := strconv.Atoi(i)
		second := sum(txtlines, one)
		if second > 0 {
			fmt.Println(one, second, one*second)
		}
	}
}
func sum(txtlines []string, one int) int {
	for _, i := range txtlines {
		second, _ := strconv.Atoi(i)
		if one+second == 2020 {
			return second
		}
	}
	return 0
}
