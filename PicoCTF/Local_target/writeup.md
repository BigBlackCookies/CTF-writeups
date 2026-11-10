# Smashing the stack so hard like it's a diddy party guest

if you don't want to do any math just use cyclic and try to narrow down where it begins to overwrite.(16 array size + 8 bytes from padding since we are on 64 bit architecture)

Insert 24 junk characters and ![A] in the end of the string which is 65 in ASCII code which triggers the win condition.

enjoy the flag
