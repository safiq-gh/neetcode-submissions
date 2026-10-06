class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        Snum = sorted(nums)
        res = []
        for i in range(len(Snum)):
            if i > 0 and Snum[i] == Snum[i - 1]:
                continue
            l,r = i + 1, len(Snum) - 1
            while l < r:
                threeSum = Snum[l] + Snum[i] + Snum[r]
                if threeSum == 0:
                    res.append([Snum[i], Snum[l], Snum[r]])
                    l += 1
                    r -= 1
                    while l < r and Snum[l] == Snum[l - 1]:
                            l += 1
                    while l < r and Snum[r] == Snum[r + 1]:
                            r -= 1
                elif threeSum > 0:
                    r -= 1
                else:
                    l += 1
        return res
