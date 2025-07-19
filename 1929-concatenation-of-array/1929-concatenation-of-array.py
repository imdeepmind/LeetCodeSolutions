class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        new_arr = []

        for _ in range(2):
            for num in nums:
                new_arr.append(num)

        return new_arr