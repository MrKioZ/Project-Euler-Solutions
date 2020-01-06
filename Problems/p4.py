"""
A palindromic number is a number that remains the same when its digits are reversed. Like 16461

This code was intentionally made in single line as a challenge not for the runtime
"""

print(max(i*e for i in range(1000,2,-1) for e in reversed(range(2,1000)) if (str(i*e)[::-1] == str(i*e)) and ((len(str(i)) + len(str(e))) == 6)))
