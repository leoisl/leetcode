### Problem link

https://leetcode.com/problems/counting-bits/

### Intuition

I got the number `2000` and transformed it into binary: `0b11111010000`. One way to divide the problem into subproblems, is to split this number in two parts, one containing the most significant bit (which is always 1 in this variable-length representation) and the rest, e.g.: `0b1` and `0b1111010000`. The number of bits in `2000` is thus `1 + number_of_bits(0b1111010000) = 1 + number_of_bits(976)`. This "rest" (`976`) is `n-2^logn`. Generalising: `number_of_bits(n) = 1 + number_of_bits(n-2^logn)`.