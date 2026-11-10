from pwn import *

p = connect('saturn.picoctf.net', 61501)

for i in range(5):
    p.recvuntil(b"Type '2' to exit the program")
    p.sendline(b'1')
    p.recvuntil(b"Please make your selection (rock/paper/scissors):")
    p.sendline(b'rockpaperscissors')

    # Eat round output
    print(p.recvline().decode().strip())  # You played: ...
    print(p.recvline().decode().strip())  # The computer played: ...
    print(p.recvline().decode().strip())  # You win! Play again?

# After 5 wins, program prints flag
p.interactive()

p.close()
