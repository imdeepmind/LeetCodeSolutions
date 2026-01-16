class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        pivot = strs[0]
        res = ""

        for c in pivot:
            delta = res + c
            is_match = True

            for word in strs[1:]:
                if not word.startswith(delta):
                    is_match = False
                    break
            
            if is_match:
                res = delta
            else:
                break
        
        return res