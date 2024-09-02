func isAnagram(s string, t string) bool {
    frequency := make(map[string]int)

    for _, c := range s {
        _, exists := frequency[string(c)]

        if exists {
            frequency[string(c)] += 1
        } else {
            frequency[string(c)] = 1
        }
    }

    for _, c := range t {
        val, exists := frequency[string(c)]

        if !exists {
            return false
        }

        if val <= 0 {
            return false
        }

        frequency[string(c)] -= 1
    }

    fmt.Println(frequency)

    for _, val := range frequency {
        if val >= 1 {
            return false
        }
    }

    return true
}