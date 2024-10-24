class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hash = {}

        for index, num in enumerate(nums):
            if num in hash:
                if abs(index - hash[num]) <= k:
                    return True
                else:
                    hash[num] = index
            else:
                hash[num] = index
        
        return False

        # for index1, num1 in enumerate(nums):
        #     for index2, num2 in enumerate(nums):
        #         if index1 != index2 and num1 == num2:
        #             if abs(index1 - index2) <= k:
        #                 return True
        
        # return False