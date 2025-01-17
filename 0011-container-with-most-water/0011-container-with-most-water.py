class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        max_water = float('-inf')

        while r > l:
            water = min(height[l], height[r]) * (r-l)

            max_water = max(max_water, water)

            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        
        return max_water