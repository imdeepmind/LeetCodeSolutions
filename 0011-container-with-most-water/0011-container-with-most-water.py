class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_capacity = float('-inf')
        i, j = 0, len(height) - 1

        while j > i:
            capacity = min(height[i], height[j]) * (j - i)

            if capacity > max_capacity:
                max_capacity = capacity
            
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        
        return max_capacity
        