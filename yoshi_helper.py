from fractions import Fraction
from itertools import takewhile
import numpy as np

def fibonacci():
    a, b = 0, 1
    while True:
        yield b
        a, b = b, a + b

def isqrt(n):
    # http://stackoverflow.com/a/15391420
    x, y = n, (n + 1) // 2
    while y < x:
        x, y = y, (y + n // y) // 2
    return x

def isprime_table(n):
    sieve = np.ones(n, dtype=bool)
    sieve[:2] = False
    for i in np.arange(2, int(n ** 0.5) + 1):
        if sieve[i]:
            sieve[i * i::i] = False
    return sieve

def primes(n):
    return np.flatnonzero(isprime_table(n)).tolist()

def nCr(n, k):
    c = Fraction(1)
    for i in range(min(k, n - k)):
        c = c * Fraction(n - i, i + 1)
    return int(c)

def zeller(q, m, y):
    # http://en.wikipedia.org/wiki/Zeller%27s_congruence
    j, k = divmod(y, 100)
    return (q + 26 * (m + 1) // 10 + k + k // 4
        + j // 4 + 5 * j) % 7

def euler_phi(n, p):
    pgen = takewhile(lambda x: x <= max(isqrt(n), 8), p)
    f, b = n, n
    while b > 1:
        x = next(pgen)
        if b % x == 0:
            f = f * (1 - Fraction(1, x))
            while b % x == 0:
                b = b / x
    return f.numerator

def factorize(n, p):
    k, b, sqrtn = 0, n, isqrt(n)
    d = {}
    while b > 1 and p[k] <= sqrtn:
        c = 0
        while b % p[k] == 0:
            b, c = b // p[k], c + 1
        if c:
            d[p[k]] = c
        k = k + 1
    return d
