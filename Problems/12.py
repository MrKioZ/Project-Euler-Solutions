from functools import reduce

def triangle_nums(x):
    return sum([i for i in range(1,x+1)])

def factors(n):
    return set(reduce(list.__add__,
                ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))

num = 2

while 1:
    triangle_num = triangle_nums(num)
    triangle_factors = factors(triangle_num)
    factors_length = len(triangle_factors)
    if factors_length > 500:
        print(str(triangle_num)+': '+str(triangle_factors))
        break

    num += 1
