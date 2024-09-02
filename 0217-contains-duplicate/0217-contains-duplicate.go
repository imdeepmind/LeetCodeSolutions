func containsDuplicate(nums []int) bool {
    hash := make(map[int]int)

    for index, value := range nums {
        _, exists := hash[value]

        if exists {
            return true
        }

        hash[value] = index
    }

    return false
}