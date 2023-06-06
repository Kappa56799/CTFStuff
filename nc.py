from pwn import *

r = remote('0.cloud.chals.io', 17969)
output = r.recvuntil(b'>')
print(output)
num = output.split(b'Question: ')[1].strip(b'\n>')
print(num)

result = eval(num)
print(result)

r.sendline(str(result))

while True:
    try:
        output = r.readline()
        print(output)
        num = output.split(b'Question: ')[1].strip(b'\n')
        print(num)
        result = eval(num)
        r.sendline(str(result))
    except:
        print(r.recvall())
        break


