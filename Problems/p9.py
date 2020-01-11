"""
An Efficient Solution can print all triplets in O(k) time where k is number of triplets printed.
The idea is to use square sum relation of Pythagorean triplet, i.e.,
addition of squares of a and b is equal to square of c, we can write these number in terms of m and n such that,

Written in one Line Intentionally for the challenge not for runtime nor simplicity
"""
a,b,c = [(a, b, c) for m in range(2, 10000) for a,b,c in [(m*m-n*n, 2*m*n, m*m+n*n) for n in range(1,m) if (m*m+n*n) < 10000] if a+b+c == 1000][0]; print(a*b*c)
