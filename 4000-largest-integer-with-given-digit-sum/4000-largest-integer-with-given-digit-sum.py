class Solution:
    def largestInteger(self, n: int, s: int) -> str:
        
        if s > 9 * n:
            return -1
    
        if s == 0:
            return 0
        
        result = []
        for _ in range(n):
    
            digit = min(s, 9)
            result.append(str(digit))
            s -= digit
            
        return int("".join(result))