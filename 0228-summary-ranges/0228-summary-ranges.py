class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        ranges = []
        current_range = []

        for i in range(len(nums)):
            if i == 0:
                current_range.append(nums[i])
            else:
                if nums[i-1] + 1 == nums[i]:
                    current_range.append(nums[i])
                else:
                    ranges.append(current_range)
                    current_range = [nums[i]]

        if current_range:
            ranges.append(current_range)

        return ["->".join([str(rng[0]), str(rng[-1])]) if len(rng) > 1 else str(rng[0]) for rng in ranges]
