## I hate my life
It's a format string vuln. You have to read several hex values from the stack to get the flag. Also mind the endianess and use llx since its on 64 bit.
The flag is on positions 13-18 and you get the values by using 

>>%{number}$llx

for each value or just make a python script to automate it.

enjoy the flag
