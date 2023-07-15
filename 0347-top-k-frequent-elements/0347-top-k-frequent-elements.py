class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash = {}
        bucket = [None] * len(nums)
        
        
        for num in nums:
            if num in hash:
                hash[num] += 1
            else:
                hash[num] = 1
        
        for key in hash.keys():
            val = hash[key] - 1
            
            if bucket[val]:
                bucket[val].append(key)
            else:
                bucket[val] = [key]
        
        res = []
        for idx, val in enumerate(reversed(bucket)):
            if val:
                for v in val:
                    res.append(v)
                    
                    if len(res) == k:
                        return res
        
        return []
