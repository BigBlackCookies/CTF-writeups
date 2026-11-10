## This challenge requires us to change the address where the binary is pointing to

After using cyclic in pwndbg to see where does the EBP begin to be overwritten I found that the offset is 44. Since the binary isn't stripped and PIE is disabled we can take the win address from symbols and construct the payload like so in the exploit file
