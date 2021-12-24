import numpy as np
import time

start = time.perf_counter()
 
def primesfrom2to(n):
    # https://stackoverflow.com/questions/2068372/fastest-way-to-list-all-primes-below-n-in-python/3035188#3035188
    """ Input n>=6, Returns a array of primes, 2 <= p < n """
    sieve = np.ones(n//3 + (n%6==2), dtype=bool)
    sieve[0] = False
    for i in range(int(n**0.5)//3+1):
        if sieve[i]:
            k=3*i+1|1
            sieve[      ((k*k)//3)      ::2*k] = False
            sieve[(k*k+4*k-2*k*(i&1))//3::2*k] = False
    return np.r_[2,3,((3*np.nonzero(sieve)[0]+1)|1)]
 
p = primes10m   = primesfrom2to(10_000_000)
s = strong10m   = [t for s, t, u in zip(p, p[1:], p[2:]) 
                   if t > (s + u) / 2]
w = weak10m     = [t for s, t, u in zip(p, p[1:], p[2:]) 
                   if t < (s + u) / 2]
b = balanced10m = [t for s, t, u in zip(p, p[1:], p[2:]) 
                   if t == (s + u) / 2]
 
print('The first 2000 strong primes:', s[:2000])
print('The count of the strong primes below 100,000,000,000:',
      sum(1 for p in s if p < 100_000_000_000))
print('The count of the strong primes below  100,000,000,000:', len(s))
print('\nThe first 2000 weak primes:', w[:2000])
print('The count of the weak primes below 100,000,000,000:',
      sum(1 for p in w if p < 100_000_000_000))
print('The count of the weak primes below 100,000,000,000:', len(w))
print('\n\nThe first 2000 balanced primes:', b[:2000])
print('The count of balanced primes below 100,000,000,000:',
      sum(1 for p in b if p < 100_000_000_000))
print('The count of balanced primes below 100,000,000,000:', len(b))
print('\nTOTAL primes below   100,000,000,000:',
      sum(1 for pr in p if pr < 100_000_000_000))
print('TOTAL primes below 100,000,000,000:', len(p))


finish = time.perf_counter()
print(f"Done in {finish - start:0.4f} seconds")

