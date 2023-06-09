from Crypto.Util.number import bytes_to_long, long_to_bytes
from Crypto import Random
import Crypto
import sys
import libnum

n1=2015805937
n2=3148630007
n3=1883043919
c1=1632893752
c2=1226329111
c3=425882503

if (len(sys.argv)>1):
    c1=int(sys.argv[1])
if (len(sys.argv)>2):
    c2=int(sys.argv[2])
if (len(sys.argv)>3):
    c3=int(sys.argv[3])
if (len(sys.argv)>4):
    n1=int(sys.argv[4])
if (len(sys.argv)>5):
    n2=int(sys.argv[5])
if (len(sys.argv)>6):
    n3=int(sys.argv[6])                
e=3



mod=[n1,n2,n3]
rem=[c1,c2,c3]

res=libnum.solve_crt(rem,mod)

print("\n\nAnswer:")
print(f"\nCipher 1: {c1}, N1={n1}")
print(f"Cipher 2: {c2}, N2={n2}")
print(f"Cipher 3: {c3}, N3={n3}")


print(f"\nWe can solve M^e with CRT to get {res}")
val=libnum.nroot(res,3)
print(f"\nIf we assume e=3, we take the third root to get: {val}")
print("Next we convert this integer to bytes, and display as a string.")
print(f"\nDecipher: {long_to_bytes(val)}")
