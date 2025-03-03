class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        pivot = strs[0]
        res = ""

        for pvc in pivot:
            match = True
            for word in strs[1:]:
                if not word.startswith(res + pvc):
                    match = False
            
            if match:
                res += pvc
            else:
                break
        
        return res
