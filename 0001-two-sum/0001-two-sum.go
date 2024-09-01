func twoSum(nums []int, target int) []int {
    numberHash := make(map[int]int)

    for index, value := range nums {
        numberHash[value] = index
    }

    for index, value := range nums {
        mapEntry, exists := numberHash[target-value]

        if exists && mapEntry != index {
            return []int{index, mapEntry}
        }
    }

    return []int{0, 0}
}