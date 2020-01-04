"""
I is a Fibonacci number if and only if 5 I**2 + 4 or 5 I**2 – 4 is a square number.
3 is a Fibonacci number since 5x3**2+4 is 49 which is 7**2
5 is a Fibonacci number since 5x5**2–4 is 121 which is 11**2

This was written in one intentionally as a challenge not for fast runtime
"""
print(sum([i for i in range(1,int(4000000)) if ((((5*(i**2)+4)**.5).is_integer()) or (((5*(i**2)-4)**.5).is_integer())) and (i%2==0)]))
