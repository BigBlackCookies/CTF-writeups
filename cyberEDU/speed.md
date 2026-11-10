### **SPEED WRITEUP**

- Using IDA Pro we can identify the logic of the binary.
- It makes use of the **rand()** and **srand()** functions. The seed for srand is found in the **nothing_here** function which is **0x11C4** which equals 4548 in decimal
- with the seed the random values generated will always repeat themselves each time we run the binary
- in the **guessing()** function we see the comparison statement between a 2nd call of rand() and a XOR of the first call of rand() declared as v1, a undeclared variable named v2 and the constant 0x539 which is 1337 in decimal
- to get the flag we just have to calculate var2 by XORing v1, 1337 and the 2nd call of rand() function, we transform the number in sha256, wrap it up in CTF{} and here's our flag

