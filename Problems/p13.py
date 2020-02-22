print(str(sum([int(line.replace('\n','')) for line in open('numbers.txt', 'r').readlines()]))[:10])
