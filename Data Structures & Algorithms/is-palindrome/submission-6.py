class Solution:
    def isPalindrome(self, s: str) -> bool:
        rev_s = ''.join([c.lower() for c in s if c.isalnum()])
        return rev_s == rev_s[::-1]