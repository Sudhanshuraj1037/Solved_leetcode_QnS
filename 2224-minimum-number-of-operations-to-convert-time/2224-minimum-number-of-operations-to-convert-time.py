class Solution:
    def convertTime(self, current: str, correct: str) -> int:
        h1, m1 = map(int, current.split(':'))
        h2, m2 = map(int, correct.split(':'))

        diff = (h2 * 60 + m2) - (h1 * 60 + m1)

        ans = 0

        for step in [60, 15, 5, 1]:
            ans += diff // step
            diff %= step

        return ans