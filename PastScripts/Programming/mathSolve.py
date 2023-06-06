from pwn import *

r = remote('byuctf.xyz', 40014)

while True:
    output = r.recvuntil(b'=')
    print(output)
    num = output.split(b'\n')[1].strip(b'=').decode()
    print(num)
    result = eval(num)
    r.sendline(str(result))
output = r.recvline(b'\n')
print(output)
r.close()
