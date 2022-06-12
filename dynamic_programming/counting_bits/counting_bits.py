import math

class Solution:
    @cache
    def recursive_count_bits(self, n: int) -> int:
        # base case
        if n==0:
            return 0
        return 1+self.recursive_count_bits(n-2**int(log(n, 2)))
    
    def countBits(self, n: int) -> List[int]:
        return [self.recursive_count_bits(i) for i in range(n+1)]
