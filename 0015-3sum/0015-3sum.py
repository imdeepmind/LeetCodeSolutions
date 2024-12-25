class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        res = []
        for index, num in enumerate(nums):
            i, j = index + 1, len(nums) - 1

            if index > 0 and num == nums[index-1]:
                continue

            while j > i:
                delta = num + nums[i] + nums[j]

                if delta == 0:
                    res.append([num, nums[i], nums[j]])
                    i += 1
                    j -= 1

                    while nums[i] == nums[i-1] and j > i:
                        i += 1
                        
                    continue
                
                if delta > 0:
                    j -= 1
                else:
                    i += 1
        
        return res