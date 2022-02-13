class Solution:
    def romanToInt(self, s: str) -> int:
        numbers = []
        mapper = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        
        for index, num in enumerate(s):
            numbers.append(mapper[num])

            if index > 0:
                if numbers[index-1] < mapper[num]:
                    numbers[index-1] *= -1
            
        return sum(numbers)

