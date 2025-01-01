from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mapper = defaultdict(list)

        for word in strs:
            res = []
            for c in word:
                res.append(c)
            
            key = "".join(sorted(res))
            mapper[key].append(word)
        
        group = []

        for _, value in mapper.items():
            group.append(value)
        
        return group
