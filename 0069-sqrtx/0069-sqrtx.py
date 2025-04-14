class Solution:
    def mySqrt(self, x: int) -> int:
        start, end = 0, x

        while end >= start:
            mid = end - ((end - start) // 2)

            if mid*mid == x:
                return mid
            
            if mid*mid > x:
                end = mid - 1
            else:
                start = mid + 1
        
        return end