class Solution:
    def isHappy(self, n: int) -> bool:
        def to_array(n):
            arr = []

            while n > 0:
                digit = n % 10
                n = n // 10

                arr.append(digit)
            
            return arr[::-1]
        
        mapper = {}

        while True:
            sqaured_arr = [x**2 for x in to_array(n)]
            sum_arr = sum(sqaured_arr)
            n = sum_arr
            
            if sum_arr in mapper:
                break

            mapper[sum_arr] = 1

            if sum_arr == 1:
                return True

        return False
