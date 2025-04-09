class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        mapper = {}

        for c in s:
            mapper[c] = mapper.get(c, 0) + 1
        
        for c in t:
            if c not in mapper:
                return False
            
            if mapper[c] > 0:
                mapper[c] -= 1

                if mapper[c] == 0:
                    del mapper[c]
        
        return len(mapper) == 0
