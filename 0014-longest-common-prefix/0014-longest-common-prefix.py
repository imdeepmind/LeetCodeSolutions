class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        pivot = strs[0]
        common = ""
        
        for idx, c in enumerate(pivot):
            for word in strs:
                if len(word) == idx or word[idx] != c:
                    return common
                
            common += c
        
        return common
            