class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""
        
        for pc in strs[0]:
            matched = True
            for word in strs[1:]:
                if not word.startswith(res + pc):
                    matched = False
                    break
            
            if matched:
                res += pc
            else:
                break
        
        return res