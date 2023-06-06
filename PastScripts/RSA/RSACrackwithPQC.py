from Crypto.Util.number import long_to_bytes
import libnum
import sys

p=954354002755510667
q=801297755486859913
c=607778777406675887172756406181993732

if (len(sys.argv)>1):
        c=int(sys.argv[1])
if (len(sys.argv)>2):
        p=int(sys.argv[2])
if (len(sys.argv)>3):
        q=int(sys.argv[3])

n = p*q
PHI=(p-1)*(q-1)

e=65537
d=(libnum.invmod(e, PHI))


res=pow(c,d, n)

print ("Cipher: ",c)
print ("p: ",p)
print ("q: ",q)

print ("\n=== Calc ===")
print ("d=",d)
print ("n=",n)
print ("Decrypt: %s" % ((long_to_bytes(res))))
