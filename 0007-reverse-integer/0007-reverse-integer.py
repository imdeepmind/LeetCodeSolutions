class Solution:
    def reverse(self, x: int) -> int:
        is_negative = False

        if x < 0:
            x = x * -1
            is_negative = True

        res = []
        
        while x:
            res.append(x % 10)
            x = x // 10
        
        s = 0

        for index, num in enumerate(res):
            s += num * (10**(len(res) - (index+1)))
        
        return s if not is_negative else s * -1