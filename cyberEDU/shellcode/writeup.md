## Classic Shellcode injection.

The details are in the exploit file. Since NX is disabled it should be a dead give away that we have to inject shellcode to win since no win function is present and doing a ret2libc is too complicated(if possible to be worth it). Multiple guides showcased padding the left side with \x00(NULL bytes) which can result in unexpected crashes sometimes(they still work for this challenge). I recomment \x90 (NOP slides) though since they are more foolproof.
