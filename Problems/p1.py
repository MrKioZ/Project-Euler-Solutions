sum = 0

for i in range(1, 1000):
    if ((i/3).is_integer() or (i/5).is_integer()):
        sum += i

print(sum)
