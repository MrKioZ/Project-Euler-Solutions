"""
To get the sum of all prime numbers that are below 2 million we can iterate from 2 to 2 million
and check the if it's prime or not using 'Mark siev[n]' Algorithm
"""
from Sieve import isPrime; print(sum(i for i in range(2,2000000) if isPrime(i)))
