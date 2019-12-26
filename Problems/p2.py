print(sum([i for i in range(1,int(4000000)) if ((((5*(i**2)+4)**.5).is_integer()) or (((5*(i**2)-4)**.5).is_integer())) and (i%2==0)]))
