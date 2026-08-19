class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        Map = {}
        for idx, num in enumerate(nums):
            diff = target - num
            if diff in Map:
                return [Map[diff], idx]
            Map[num] = idx