class Solution:
    def isPalindrome(self, s: str) -> bool:
        rev_s = ""
        for idx in range(len(s) - 1, -1, -1):
            if s[idx].strip().isalnum():
                rev_s+=s[idx]
        return  rev_s[::-1].lower() == rev_s.lower()