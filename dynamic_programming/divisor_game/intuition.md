# Problem link

https://leetcode.com/problems/divisor-game/

# Intuition

Given that players play optimally, this means that they go through all 0 < x < n and check if there is an x such that if they play, the other player will surely lose. We know by the base cases that when a player has to play and n=2 they will surely win, and if n=3 they will surely lose. For n=4, we can try x=1 and x=2. If we play x=1, then Bob will play with n=3, and he will surely lose, and thus we win. For n=5, the only option is play x=1, and the Bob will play with n=4 and he will surely win. For n=6+, we can recursively knows who wins (this is actually true for n>3). Thus Alice wins for a given n if there is an x such that Bob loses with n-x.