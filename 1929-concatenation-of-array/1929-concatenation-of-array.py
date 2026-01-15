class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        _res = []

        for _ in range(2):
            for num in nums:
                _res.append(num)
        
        return _res