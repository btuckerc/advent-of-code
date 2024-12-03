package main

import (
    "bufio"
    "fmt"
    "os"
    "strings"
)

func part1(input []string) int {
    // TODO: Implement part 1
    return 0
}

func part2(input []string) int {
    // TODO: Implement part 2
    return 0
}

func readInput(filename string) ([]string, error) {
    file, err := os.Open(filename)
    if err != nil {
        return nil, err
    }
    defer file.Close()

    var lines []string
    scanner := bufio.NewScanner(file)
    for scanner.Scan() {
        lines = append(lines, strings.TrimSpace(scanner.Text()))
    }
    return lines, scanner.Err()
}

func main() {
    input, err := readInput("input.txt")
    if err != nil {
        fmt.Println("Using example.txt")
        input, err = readInput("example.txt")
        if err != nil {
            fmt.Fprintf(os.Stderr, "Failed to read input: %v\n", err)
            os.Exit(1)
        }
    }

    fmt.Printf("Part 1: %d\n", part1(input))
    fmt.Printf("Part 2: %d\n", part2(input))
}
