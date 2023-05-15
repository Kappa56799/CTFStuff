from pwn import *

r = remote('static-01.heroctf.fr', 8000)
output = r.recvuntil(b'?\n')

while True:
    try:
        output = r.recv(213)
        print(output)
        num = output.split(b'\n')[1].decode()
        print(num)
        result = eval(num)
        r.sendline(str(result)).encode()
    except:
        print(r.recvall().decode().strip().split('\n')[-1])
        break

