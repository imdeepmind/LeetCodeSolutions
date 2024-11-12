class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = 0

        start, end = 0, len(height) - 1

        while end > start:
            delta = min(height[start], height[end]) * (end - start)

            if delta > max_area:
                max_area = delta

            if height[start] > height[end]:
                end -= 1
            else:
                start += 1

        return max_area