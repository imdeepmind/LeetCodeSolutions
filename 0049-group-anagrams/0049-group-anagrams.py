class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        freq_s = {}
        freq_t = {}
        
        for c in s:
            if c in freq_s:
                freq_s[c] += 1
            else:
                freq_s[c] = 1
        
        for c in t:
            if c in freq_t:
                freq_t[c] += 1
            else:
                freq_t[c] = 1
                
        for key in freq_s:
            if not key in freq_t or freq_t[key] != freq_s[key]:
                return False
        
        return True
    
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash = defaultdict(list)
        
        for s in strs:
            hash["".join(sorted(s))].append(s)
        
        return hash.values()
    
#         anagrams = []
#         used_words = []
        
#         for idx1, x in enumerate(strs):
#             if x not in used_words:
#                 matches = []

#                 for idx2, y in enumerate(strs):
#                     if idx1 != idx2 and y not in used_words:
#                         if self.isAnagram(x, y):
#                             matches.append(y)

#                 used_words.append(x)
#                 for w in matches:
#                     used_words.append(w)

#                 anagrams.append([
#                     x, *matches
#                 ])
        
#         return anagrams
