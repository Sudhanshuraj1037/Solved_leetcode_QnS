class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        temp = x
        total = 0

        while temp > 0:
            digit = temp % 10
            total += digit
            temp //= 10

        if x % total == 0:
            return total
        else:
            return -1