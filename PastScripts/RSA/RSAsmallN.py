from Crypto.Util.number import long_to_bytes,bytes_to_long
from Crypto import Random
import Crypto
import sys
import libnum
from math import isqrt

from sympy import *
import random

def get_prime(bits):
	p = Crypto.Util.number.getPrime(bits, randfunc=Crypto.Random.get_random_bytes)
	return(p)

# Rational numbers have finite a continued fraction expansion.
def get_cf_expansion(n, d):
    e = []
    q = n // d
    r = n % d
    
    e.append(q)

    while r != 0:
        n, d = d, r           
        q = n // d
        r = n % d
        e.append(q)

    return e

def get_convergents(e):
    n = [] # Nominators
    d = [] # Denominators

    for i in range(len(e)):
        if i == 0:
            ni = e[i]
            di = 1
        elif i == 1:
            ni = e[i]*e[i-1] + 1
            di = e[i]
        else: # i > 1 
            ni = e[i]*n[i-1] + n[i-2]
            di = e[i]*d[i-1] + d[i-2]

        n.append(ni)
        d.append(di)
        yield (ni, di)



e=48597374700452521550982311087817119639997459040470423165359113070286349495771
N = 53142908692405444892952644138150097840092206295779523619518972915705070189107
C=1323006441239439900342917619206596179147814147487118324330272843733108187575

     
if (len(sys.argv)>1):
        C=int(sys.argv[1])
if (len(sys.argv)>2):
        e=int(sys.argv[2])
if (len(sys.argv)>3):
        N=int(sys.argv[3])


print(f'Bob uses RSA to send an encrypted message to Alice. The public exponent (e) is {e} and the modulus (N) is {N}. With a cipher of {C}, determine the decrypted message:')

cf_expansion = get_cf_expansion(e, N)
convergents = get_convergents(cf_expansion)

for pk, pd in convergents: # pk - possible k, pd - possible d
	if pk == 0:
		continue;

	possible_phi = (e*pd - 1)//pk

	p = Symbol('p', integer=True)
	roots = solve(p**2 + (possible_phi - N - 1)*p + N, p)

	if len(roots) == 2:
		pp, pq = roots # pp - possible p, pq - possible q
		if pp*pq == N:
			print('\nAnswer:')
			print('Using Wiener attack')
			d=pow(e,-1,possible_phi)
			print('Found d:',d)
			print('Found p:',pp)
			print('Found q:',pq)
			print('Found PHI:',possible_phi)
			print('Now using C^d mod N')
			M=pow(C,d,N)
			print(f"\nDecipher: {long_to_bytes(M)}")
			sys.exit(0)

print('[-] Wiener\'s Attack failed; Could not factor N')
sys.exit(1)
