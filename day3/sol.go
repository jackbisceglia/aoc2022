package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
)

func readInput() []string {
	lines := []string{}
	f, err := os.Open("input.txt")

	if err != nil {
		log.Fatal(err)
	}

	defer f.Close()

	scanner := bufio.NewScanner(f)
	for scanner.Scan() {
		lines = append(lines, scanner.Text())
	}

	return lines
}

func contains(s string, e rune) bool {
	for _, a := range s {
		if a == e {
			return true
		}
	}
	return false
}

func priority(char rune) int {
	ascii := int(char)

	if ascii >= 97 && ascii <= 122 {
		return ascii - int('a') + 1
	} else {
		return ascii - int('A') + 27
	}
}

func pt1() {
	lines := readInput()
	total := 0

	for _, line := range lines {
		sack1 := line[0 : len(line)/2]
		sack2 := line[len(line)/2:]

		for _, char := range sack2 {
			if contains(sack1, char) {
				total += priority(char)
				break
			}
		}
	}

	fmt.Printf("Total: %d", total)
}

func main() {
	fmt.Println("Part 1:")
	pt1()
}
