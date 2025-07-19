from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def get_key(word):
            return "".join(sorted(word))
        
        mapper = defaultdict(list)

        for word in strs:
            mapper[get_key(word)].append(word)
        
        resp = []

        for key, value in mapper.items():
            resp.append(value)
        
        return resp
                

