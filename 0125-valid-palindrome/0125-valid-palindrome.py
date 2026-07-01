class Solution:
    def isPalindrome(self, s: str) -> bool:
        def is_valid(ch):
            ascii_value = ord(ch)

            if 48 <= ascii_value <= 57:
                return True
            if 65 <= ascii_value <= 90:
                return True
            if 97 <= ascii_value <= 122:
                return True
            return False

        s = s.lower()
        left = 0
        right = len(s) - 1

        while left < right:
            if not is_valid(s[left]):
                left += 1
            elif not is_valid(s[right]):
                right -= 1
            elif s[left] != s[right]:
                return False
            else:
                left += 1
                right-= 1
        return True