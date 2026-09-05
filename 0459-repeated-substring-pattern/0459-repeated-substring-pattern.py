class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        n = len(s)

        for i in range(1, n):
            if n % i == 0:
                part = s[:i]

                if part * (n // i) == s:
                    return True

        return False