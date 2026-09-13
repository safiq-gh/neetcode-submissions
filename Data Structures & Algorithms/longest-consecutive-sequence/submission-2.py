class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        map = set(nums)
        longest = 0
        for num in map:
            if num - 1 not in map:
                curr = 1
                while num + curr in map:
                    curr += 1
                longest = max(longest, curr)
        return longest