## Simple challenge where we have to overwrite a variable with our values

This little app brags that is very secure. Managed to put my hands on the source code, but I am bad at pwn. Can you do it for me please? Thx.

Flag format: ctf{sha256}

# I didn't get the source code but ok i guess

Looking in Ghidra first thing I see the program reads the flag for me if [local_c] has a specific value.
Seeing how we can input a string into local_58, the program uses gets(unlimited reading size despite the buffer size) and local_c is declared right below it I deduced that they might be on the stack one next to the other meaning if I overwrite local_58 with 76 junk chars and append [l33t] to the string I can overwrite local_c (no GDB or pwntools needed).

# It seems I was RIGHT :D
Opening the online service and sending the payload gave the flag.
