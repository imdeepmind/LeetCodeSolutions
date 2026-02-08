class Solution:
    def mySqrt(self, x: int) -> int:
        start, end = 1, x

        while end >= start:
            mid = start + ((end - start) // 2)

            if mid ** 2 > x:
                end = mid - 1
            elif mid ** 2 < x:
                start = mid + 1
            else:
                return mid
        
        return end