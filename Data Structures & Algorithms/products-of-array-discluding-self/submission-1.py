class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [0] * len(nums)
        suffix = [0] * len(nums)
        res = [0] * len(nums)
        prefix[0] = suffix[-1] = 1
        for i in range(1,len(prefix)):
            prefix[i] = prefix[i - 1] * nums[i - 1]
        for j in range(len(suffix) - 2,-1, -1):
            suffix[j] = suffix[j + 1] * nums[j + 1]
        for i in range(len(res)):
            res[i] = prefix[i] * suffix[i]
        return res
