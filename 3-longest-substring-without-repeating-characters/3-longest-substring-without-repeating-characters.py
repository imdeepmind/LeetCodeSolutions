class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        
        max_length = 1
        max_substr = ""
        
        for i, c1 in enumerate(s):
            max_substr = c1
            
            for j, c2 in enumerate(s[i+1:]):
                if c2 in max_substr:
                    max_substr = ""
                    break
                else:
                    max_substr += c2
            
                if len(max_substr) > max_length:
                    max_length =  len(max_substr)
        
        return max_length
