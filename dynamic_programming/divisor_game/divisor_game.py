class Solution:
    @cache
    def divisorGame(self, n: int) -> bool:
        # base cases
        if n==2:
            return True
        if n==3:
            return False
        
        current_player_wins = any((not self.divisorGame(n-i) for i in range(1, n) if n%i==0))
        return current_player_wins
