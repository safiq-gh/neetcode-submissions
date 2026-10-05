class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        mapp = set(nums)
        for num in mapp:
            if num - 1 not in mapp:
                curr = 1
                while num + 1 in mapp:
                    curr += 1
                    num += 1
                longest = max(longest, curr)
        return longest