class Solution:
    def trap(self, height: List[int]) -> int:
        rain_water = 0
        l,r = 0, len(height) - 1
        maxLeft, maxRight = height[l], height[r] 
        while l < r:
            # rain_water += min(max(maxLeft, height[l]), max(maxRight, height[r]))
            if height[l] <= height[r]:
                if height[l] < maxLeft:
                    rain_water += maxLeft - height[l]
                maxLeft = max(maxLeft, height[l])
                l += 1
            else:
                if height[r] < maxRight:
                    rain_water += maxRight - height[r]
                maxRight = max(maxRight, height[r])
                r -= 1
        return rain_water





