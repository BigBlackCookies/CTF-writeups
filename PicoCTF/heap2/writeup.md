# Next installment of The Heap Trilogy that should make new people struggle but is hassle-free with pwntools

The overwrite size is still 32 bytes of junk + our payload but this time we use ![function pointers] meaning we have to overwrite safe_var with the address of the win function in order to get the flag. The included python script does everything for you including retrieving the ![win] function from symbols, making the payload and navigating the menu for you. Enjoy the flag :)
