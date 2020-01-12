def SieveOfAtkin(limit):

    # 2 and 3 are known
    # to be prime
    if (limit > 2):
        print(2 , end = " ")
    if (limit > 3):
        print(3 , end = " ")

    # Initialise the sieve
    # array with False values
    sieve = [False] * limit
    for i in range( 0 , limit ):
        sieve[i] = False

    '''Mark siev[n] is True if
    one of the following is True:
    a) n = (4*x*x)+(y*y) has odd
    number of solutions, i.e.,
    there exist odd number of
    distinct pairs (x, y) that
    satisfy the equation and
    n % 12 = 1 or n % 12 = 5.
    b) n = (3*x*x)+(y*y) has
    odd number of solutions
    and n % 12 = 7
    c) n = (3*x*x)-(y*y) has
    odd number of solutions,
    x > y and n % 12 = 11 '''
    x = 1
    while(x * x < limit ) :
        y = 1
        while(y * y < limit ) :

            # Main part of
            # Sieve of Atkin
            n = (4 * x * x) + (y * y)
            if (n <= limit and (n % 12 == 1 or
                                n % 12 == 5)):
                sieve[n] ^= True

            n = (3 * x * x) + (y * y)
            if (n <= limit and n % 12 == 7):
                sieve[n] ^= True

            n = (3 * x * x) - (y * y)
            if (x > y and n <= limit and
                          n % 12 == 11):
                sieve[n] ^= True
            y += 1
        x += 1

    # Mark all multiples of
    # squares as non-prime
    r = 5
    while(r * r < limit) :
        if (sieve[r]) :
            for i in range(r * r, limit, r * r):
                sieve[i] = False

    # Print primes
    # using sieve[]
    for a in range(5 , limit ):
        if (sieve[a]):
            print(a , end = " ")


def SieveOfEratosthenes(n):

    # Create a boolean array "prime[0..n]" and initialize
    #  all entries it as true. A value in prime[i] will
    # finally be false if i is Not a prime, else true.
    prime = [True for i in range(n+1)]
    p = 2
    while (p * p <= n):

        # If prime[p] is not changed, then it is a prime
        if (prime[p] == True):

            # Update all multiples of p
            for i in range(p * p, n+1, p):
                prime[i] = False
        p += 1

    # Returns all Primes
    for p in range(2, n):
        if prime[p]:
            yield p

if __name__=='__main__':

    n = (10**6)*2 # 2 Million
    print(sum(i for i in SieveOfEratosthenes(n))) #Prints the Sum of Prime numbers that are below 2 million
