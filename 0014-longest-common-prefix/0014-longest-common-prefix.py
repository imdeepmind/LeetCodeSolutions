class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 1:
            return strs[0]
        
        common = ""
        for index, ch in enumerate(strs[0]):
            for word in strs[1:]:
                if len(word) <= index:
                    return common
                if word[index] != ch:
                    return common
                
            common += ch
        
        return common