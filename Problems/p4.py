"""
A palindromic number is a number that remains the same when its digits are reversed. Like 16461

This code was intentionally made in single line as a challenge not for the runtime
"""

print(max(a*b for a in range(9999, 100, -1) for b in range(a, 100, -1) if str(a*b) == str(a*b)[::-1]))
