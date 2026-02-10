class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        pivot = strs[0]
        res = ""

        for c in pivot:
            is_match = True
            for word in strs[1:]:
                if not word.startswith(res + c):
                    is_match = False
                    break
            
            if is_match:
                res += c
            else:
                break
        
        return res