## This binary adds on from the previous one by asking us to also load function arguments on the stack

My first thought was how could I load the required function arguments on the stack. Checking the binary with the [file] command shows us its on 32-bit architecture meaning function arguments are directly loaded on the stack compared to 64-bit where you mostly use specified registers. 

First we have to determine the offset to overwrite [EIP] which we can do using a huge cyclic pattern and finding the number of junk characters needed to be inserted before changing the pointer. This time 112 is the sweet spot. 

After reaching the [win] function I remembered I had to also load the arguments. I inserted another cyclic pattern to test where does the overwrite begin and I found that after another 4 bytes of junk we can send our two arguments one after the other. The first [0xcafef00d] was at [EBP - 8] and the second at [EBP - 0xc],0xc being hex for 12. 

This makes sense since on 32-bit architecture and we get 4 bytes of padding as a method to keep the stack aligned.

The payload is in the exploit file enjoy the flag.
