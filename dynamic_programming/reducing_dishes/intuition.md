### Problem link

https://leetcode.com/problems/reducing-dishes/

### Intuition

The hard part here is just finding the optimal substructure of the problem. The trick is just looking at the examples and realising that, if the answer has n dishes, the n most-valued dishes are there in such a order that the most valued dish is the last (and thus get more weight). So basically sort the dishes by value, and find the best solution with just a single dish (i.e. just the most-valued dish), then with 2 dishes (2nd-most-valued and then most-valued) and so on. This is not dynamic programming though... at least my solution