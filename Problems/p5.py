print([num for num in range(20, 300000000, 20) if all(num % n == 0 for n in [11, 13, 14, 16, 17, 18, 19, 20])][0])
