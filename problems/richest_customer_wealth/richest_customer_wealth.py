# https://leetcode.com/problems/richest-customer-wealth

def richest_customer_wealth(accounts: list[list[int]]) -> int:
    max_wealth = 0
    
    for i in range(0, len(accounts)):
        wealth = 0
        for j in range(0, len(accounts[0])):
            wealth += accounts[i][j]
        
        if wealth > max_wealth:
            max_wealth = wealth
    
    return max_wealth
