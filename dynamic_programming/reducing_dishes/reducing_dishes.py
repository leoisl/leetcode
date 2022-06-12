class Solution:
    def max_sat(self, n, sorted_dishes):
        max_sat_for_n_dishes=0
        for i in range(1, n+1):
            max_sat_for_n_dishes+=sorted_dishes[i-1]*(n-i+1)
        return max_sat_for_n_dishes
    
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        sorted_dishes=sorted(satisfaction, reverse=True)
        return max(self.max_sat(i, sorted_dishes) for i in range(len(sorted_dishes)+1))