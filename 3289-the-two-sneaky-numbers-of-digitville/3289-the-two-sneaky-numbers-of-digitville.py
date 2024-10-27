class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        hash = {}

        for num in nums:
            if num in hash:
                hash[num] += 1
            else:
                hash[num] = 1
        
        ans = []
        for k in hash:
            if hash[k] > 1:
                ans.append(k)

        return ans