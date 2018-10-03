#!/bin/python3
# summation function
import sys
def sig(p):
    return(p*(p+1)//2)
  

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    x=(n-1)//3
    y=(n-1)//5
    z=(n-1)//15
# sum of mutiples of 3 + sum of multiples of 5 - sum of multiples of 15 to exclude repeated cases.
    print((3*sig(x))+(5*sig(y))-(15*sig(z)))
