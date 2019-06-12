from functools import reduce
from math import gcd
from sympy import mod_inverse
from random import randint


# Calculate the Least Common Multiple (LCM) value
def lcm(a, b):
    return int(a * b / gcd(a, b))


# *** Paillier Cryptosystem ***
# The L function
def L(u):
    return int((u - 1) / n)


# Generates a random R value for encryption process
def select_random_r():
    r = randint(1, n - 1)
    if (gcd(r, n) != 1):
        return select_random_r()
    return r


# Encryption Function
def encrypt(m, r):
    c = ((g ** m) * (r ** n)) % (n ** 2)
    return c


# Decryption Function
def decrypt(c):
    return (L((c ** lm) % (n ** 2)) * mu) % n


p = 13
q = 11

g = 67  # Public
n = p * q  # Public

lm = lcm(p - 1, q - 1)  # Private
mu = mod_inverse(L((g ** lm) % (n ** 2)), n)  # Private

# Encryption:
m1 = 11  # Message m1 to encrypt
print("m1: " + str(m1))
r1 = select_random_r()
c1 = encrypt(m1, r1)
print("r1: " + str(r1))
print("c1 (Encrypted m1): " + str(c1) + "\n")

m2 = 22  # Message m2 to encrypt
print("m2: " + str(m2))
r2 = select_random_r()
c2 = encrypt(m2, r2)
print("r: " + str(r2))
print("c2 (Encrypted m2): " + str(c2) + "\n")

# Decryption:
print("Decrypted c1: " + str(decrypt(c1)))
print("Decrypted c2: " + str(decrypt(c2)))
