class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        suff_max = [prices[-1]] * len(prices)
        for i in range(len(prices) - 2, -1, -1):
            suff_max[i] = max(prices[i], suff_max[i+1])
        
        max_prof = 0
        for i in range(len(prices)):
            max_prof = max(max_prof, suff_max[i] - prices[i])
        
        return max_prof