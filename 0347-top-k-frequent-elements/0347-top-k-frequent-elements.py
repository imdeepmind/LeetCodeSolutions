class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash = {}

        for num in nums:
            if num in hash:
                hash[num] += 1
            else:
                hash[num] = 1
        
        bucket = [[] for i in range(len(nums))]

        for key, value in hash.items():
            bucket[value-1].append(key)
        
        resp = []
        for i in range(len(bucket)-1, -1, -1):
            for item in bucket[i]:
                resp.append(item)
        
        return resp[:k]
