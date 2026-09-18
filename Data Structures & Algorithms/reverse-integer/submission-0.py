class Solution:
    def reverse(self, x: int) -> int:
        sign = 1
        rev = 0
        if x < 0:
            sign = -1
            x = x * -1
        while x > 0:
            n = x % 10
            x = x // 10
            rev = rev * 10 + n
            if not (-2**31) <= rev <= (2**31 - 1):
                return 0
        return rev * sign