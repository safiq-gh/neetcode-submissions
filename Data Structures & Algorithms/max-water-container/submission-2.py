class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left, right = 0, len(heights) - 1
        maximum = 0
        while left < right:
            curr_water = min(heights[left], heights[right]) * (right - left)
            maximum = max(maximum, curr_water)
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
        return maximum
