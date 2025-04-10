class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        pivot = strs[0]
        res = ""

        for p in pivot:
            matched = True

            for word in strs[1:]:
                if not word.startswith(res + p):
                    matched = False

            if matched:
                res += p
            else:
                break
            
        return res