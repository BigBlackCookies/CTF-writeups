# Heap 0 is a simple pwn challenge that teaches us about heap overflow
> The binary uses malloc to define size of a string array instead of the usual predefined number size but as always the size is much more than needed. Enabling us to overwrite data
> I suppose you could waste time calculating distance but the binary isn't stripped so a ![nm] shows us the offset between the input and the value we have to overwrite is two. just to make sure all you have to do is hop on pwndgb, use ![cyclic 200], input it and get the flag
