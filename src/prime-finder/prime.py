#!/usr/bin/env python3

import time
import numpy as np

n = int(input("Enter a Number: "))
x = int(input(f"How many primes under {n} should be displayed? "))

start = time.perf_counter()


def primes_from_2_to(n):
    # https://stackoverflow.com/questions/2068372/fastest-way-to-list-all-primes-below-n-in-python/3035188#3035188
    sieve = np.ones(n // 3 + (n % 6 == 2), dtype=bool)
    sieve[0] = False
    for i in range(int(n**0.5) // 3 + 1):
        if sieve[i]:
            k = 3 * i + 1 | 1
            sieve[((k * k) // 3)::2 * k] = False
            sieve[(k * k + 4 * k - 2 * k * (i & 1)) // 3::2 * k] = False
    return np.r_[2, 3, ((3 * np.nonzero(sieve)[0] + 1) | 1)]


p = primes1b = primes_from_2_to(n)
s = strong1b = [t for s, t, u in zip(p, p[1:], p[2:]) if t > (s + u) / 2]
w = weak1b = [t for s, t, u in zip(p, p[1:], p[2:]) if t < (s + u) / 2]
b = balanced1b = [t for s, t, u in zip(p, p[1:], p[2:]) if t == (s + u) / 2]

print(f"\nThe count of the strong primes below {n}: {len(s)}")
print(f"The first {x} strong primes: {s[:x]}")
print(f"\nThe count of the weak primes below {n}: {len(w)}")
print(f"The first {x} weak primes: {w[:x]}")
print(f"\nThe count of balanced primes below {n}: {len(b)}")
print(f"The first {x} balanced primes: {b[:x]}")
print(f"\nCount of all primes below {n}: {len(p)}")

finish = time.perf_counter()
print(f"Done in {finish- start:0.4f} seconds")
