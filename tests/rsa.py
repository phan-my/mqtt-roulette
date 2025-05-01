from random import randint, choice
from math import sqrt, floor, log2
import math
UPPER = 10**22 + 1
UPPER_RANDOM = 10**16

def powermod(n, exponent, m):
    # n**exponent % m
    bitLength = int(floor(log2(exponent) + 1))

    Equiv = []

    out = 1
    Equiv.append(n % m)

    for i in range(1, bitLength + 1):
        Equiv.append((Equiv[i - 1]**2) % m)

        if is_odd(exponent):
            out *= Equiv[i - 1]
            out = out % m
        
        exponent = exponent >> 1
    
    return (out + m) % m

def is_prime(n):
    Primes = [int(x) for x in open("Primes").read().split()]
    divisors = 0
    
    if n == 0 or n == 1:
        return False
    
    if n in Primes:
        return True

    for i in range(1, int(sqrt(n) + 1)):
        if n % i == 0:
            divisors += 1
            if divisors > 1:
                return False
    
    return True

# check natural for odd parity
def is_odd(n):
    if n & 1:
        return True
    return False

# Miller-Rabin
# n must be odd, please ftlog
def is_probable_prime(n):
    if n == 2:
        return True
    if not n & 1:
        print("what did i tell u? n must be odd.")
        return False

    # s > 0 and d odd > 0 where n - 1 = 2^{s}d
    s = 1
    d = 1

    while n - 1 != 2**s * d:
        if (n - 1) % 2**s == 0:
            if is_odd(int((n - 1) / 2**s)):
                d = int((n - 1) / 2**s)
                continue
        d = 1
        s += 1
#        print("s, d:", s, d)

#    print("n, s, d:", n, s, d)

    # main loop
    k = 64
    for i in range(k):
        a = randint(2, n - 2)
        x = powermod(a, d, n)
        for j in range(s):
            y = powermod(x, 2, n)
            # nontrivial sqrt(1) % n
            if y == 1 and x != 1 and x != n - 1:
                return False
            x = y
        if y != 1:
            return False
    return True

"""n = 10**22 + 1
if is_probable_prime(n):
    tmp = "True"
else:
    tmp = "False"
print(n, tmp)
"""

def random_prime(minPrime, maxPrime):
    if maxPrime <= 999983:
        Primes = [int(x) for x in open("Primes").read().split()]
        return choice(Primes)
    else:
        r = 1
        while is_prime(r) == False:
            r = randint(minPrime, maxPrime)
        return r

def random_probable_prime(minPrime, maxPrime):
    # for very small primes
    Primes = [int(x) for x in open("Primes").read().split()]
    if maxPrime <= 999983:
        return choice(Primes)

    smallPrime = False
    while True:
        out = randint(minPrime, maxPrime)
        # check for first few primes
        for i in range(10):
            if out % Primes[i] == 0:
                smallPrime = True
                break
        if smallPrime:
            smallPrime = False
            continue
#        print("attempt", out)
        if is_probable_prime(out):
            return out

# print(random_probable_prime(10**15, UPPER_RANDOM))

# Sieve of Eratosthenes
# Code by David Eppstein, UC Irvine, 28 Feb 2002
# http://code.activestate.com/recipes/117119/

def gen_primes(high):
    """ Generate an infinite sequence of prime numbers.
    """
    # Maps composites to primes witnessing their compositeness.
    # This is memory efficient, as the sieve is not "run forward"
    # indefinitely, but only as long as required by the current
    # number being tested.
    #
    D = {}
    
    # The running integer that's checked for primeness
    q = 2
    
    while q < high:
        if q not in D:
            # q is a new prime.
            # Yield it and mark its first multiple that isn't
            # already marked in previous iterations
            # 
            yield q
            D[q * q] = [q]
        else:
            # q is composite. D[q] is the list of primes that
            # divide it. Since we've reached q, we no longer
            # need it in the map, but we'll mark the next 
            # multiples of its witnesses to prepare for larger
            # numbers
            # 
            for p in D[q]:
                D.setdefault(p + q, []).append(p)
            del D[q]
        
        q += 1

def phi_prime(p, q):
    return (p - 1)*(q - 1)

def gcd(a, b):
    while b != 0:
        tmp = a
        a = b
        b = tmp % b

    return a

def extended_gcd_b(a, b):
    n = a
    r1 = a
    r = b

    Q = []

    i = 0

    # where is do while in python???
    n = r1
    r1 = r
    Q.append(floor(n//r1))
    r = n % r1
    i += 1
    while r != 0:
        n = r1
        r1 = r
        Q.append(floor(n//r1))
        r = n % r1
        i += 1
    
    i -= 2

    nA = 1
    nB = -Q[i]

    while i > 0:
        tmp = nA
        nA = nB
        nB = -Q[i - 1]*nB + tmp
        i -= 1
    
    return nB

"""
# extended_gcd_b(935663215469784531469785978253164231314567851467851478615682314564456231546823145682314567823152935663215469784531469785978253164231314567851467851478615682314564456231546823145682314567823152935663215469784531469785978253164231314567851467851478615682314564456231546823145682314567823152935663215469784531469785978253164231314567851467851478615682314564456231546823145682314567823152935663215469784531469785978253164231314567851467851478615682314564456231546823145682314567823152935663215469784531469785978253164231314567851467851478615682314564456231546823145682314567823152935663215469784531469785978253164231314567851467851478615682314564456231546823145682314567823152935663215469784531469785978253164231314567851467851478615682314564456231546823145682314567823152, 9356632154697845314697859782531642313145678514678514786156823145644562315468231456823145678231525231546324156256342314678145682534652346578434156430214562104864935663215469784531469785978253164231314567851467851478615682314564456231546823145682314567823152523154632415625634231467814568253465234657843415643021456210486493566321546978453146978597825316423131456785146785147861568231456445623154682314568231456782315252315463241562563423146781456825346523465784341564302145621048649356632154697845314697859782531642313145678514678514786156823145644562315468231456823145678231525231546324156256342314678145682534652346578434156430214562104864)
a = 123
b = 456
print("mod =", extended_gcd_b(a, b))
print("gcd =", gcd(a, b))

Primes = []

for q in gen_primes(maxPrime):
    Primes.append(q)

print(choice(Primes))
"""

# Key generation
minPrime = 2**32
maxPrime = UPPER_RANDOM
p = random_probable_prime(minPrime, maxPrime)
q = random_probable_prime(minPrime, maxPrime)
n = p*q
phi = phi_prime(p, q)

e = phi
while gcd(phi, e) != 1:
    e = randint(1, phi)

d = phi + extended_gcd_b(phi, e)

print("PRIVATE.")
print("p*q = " + str(p) + "*\n\t" + str(q))
print("phi = " + str(phi))
print("d = " + str(d))
print("")

print("Public.")
print("n = " + str(n))
print("e = " + str(e))

print("d*e equiv", d*e % phi, "mod phi")

m = 0xFFFFFFFFFFFFFFFFFFFFFFFF
c = powermod(m, e, n)

print("Encrypted text: " + str(c))
print("Plaintext: " + str(powermod(c, d, n)))