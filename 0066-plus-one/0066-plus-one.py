class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if digits[-1] < 9:
            digits[-1] += 1
            
            return digits
        
        digits[-1] = 0
        
        if len(digits) > 1:
            return self.plusOne(digits[:-1]) + [digits[-1]]
        
        return [1] + digits
        