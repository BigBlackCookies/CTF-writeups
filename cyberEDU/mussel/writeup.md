## This is a by-the-books ROP chain exploit

First came the recon phase which was pretty straight forward. After ['Hello'] there was a buffer overflow vuln.

Since no helper function is present we have to pop a shell using the ['ret2libc'] method.

#---> Step 1: leak the libc address
We have to overflow the buffer and call puts with the [GOT] puts entry as input. Since we are on 64 bits we first need to pop the register that holds the puts argument and replace it with puts@got and then jump back to main to execute the 2nd stage exploit

#---> Step 1.5: Finding out the libc version

I recommend when you do this to do it on the online service itself directly instead of the local binary since most CTF challs compile the binary they give you with a different libc version because they like to waste your time.

Because puts gave too many options I narrowed it down doing the same for the other GOT entries by running the 1st half of the exploit against the service multiple times with different functions(change it from p64(e.got['puts']) to p64(e.got['setvbuf']) or whatever) and I narrowed it down to one libc version. After this the work was trivial

#---> Step 2: Popping a shell

Following <a href="https://ir0nstone.gitbook.io/notes/binexp/stack/return-oriented-programming/ret2libc"> this guide </a> I managed to craft the payload fairly easily and got the flag

