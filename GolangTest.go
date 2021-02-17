package main

import "fmt"

func main() {
    // input1 := 5
    input2 := []int{}
    dif := 0

    // find difference between smallest and
    // biggest which are next to each other

    for i := 1; len(input2) > i; i++ {
        if input2[i-1] > input2[i] && dif < input2[i-1]-input2[i] {
            dif = input2[i-1] - input2[i]
        }
    }

    fmt.Println("Input2:", input2)
    // run through 'dif' amount of times.
    for i := 0; i < dif; i++ {
        for j := 1; len(input2) > j; j++ {
            if input2[j-1] > input2[j] {
                input2[j]++
            }
        }
        fmt.Println("Working...:", input2)
    }
    fmt.Printf("Finished with %v cycles.\nResult:%v\n", dif, input2)
}