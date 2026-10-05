class Solution:
    def isPalindrome(self, s: str) -> bool:
        rev_s = ''.join([c.lower() for c in s if c.isalnum()])
        if rev_s == rev_s[::-1]:
            return True
        return False