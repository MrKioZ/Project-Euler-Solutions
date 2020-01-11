a,b,c = [(a, b, c) for m in range(2, 10000) for a,b,c in [(m*m-n*n, 2*m*n, m*m+n*n) for n in range(1,m) if (m*m+n*n) < 10000] if a+b+c == 1000][0]; print(a*b*c)
