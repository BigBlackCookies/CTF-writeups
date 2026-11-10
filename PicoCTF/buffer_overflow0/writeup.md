## Simple challenge which should make an intro to buffer_overflows

All we have to do is corrupt rbp with our input which is easy since we are given a 100 byte buffer which gets copies to a 16 byte buffer and enables us to overflow. Since we are on 32-bit architecture the rbp location is at ![buffer size + 4] which lets us know that sending 20 characters is enough to overflow.
After overflowing with junk characters we get the flag
