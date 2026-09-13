class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        Snums = set(nums)
        longest = 0
        for num in Snums:
            if num - 1 not in Snums:
                curr = 1
                while num + curr in Snums:
                    curr += 1
                longest = max(longest,curr)
        return longest