class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        wealth = 0
        for customer in accounts:
            customerWealth=0
            for j in customer:
                customerWealth += j
                wealth=max(wealth, customerWealth)
        return wealth
        
                