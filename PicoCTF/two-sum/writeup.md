## Very basic introductory integer overflow

The main hint to guide ouselves is [What two positive numbers can make this possible: n1 > n1 + n2 OR n2 > n1 + n2]. Normally this would be impossible but since we are in C math has a funny way to work when we go out of bounds. Since both numbers are declared as int and the limit for an int is [-2147483647 <==> 2147483647] if we add 1 to 2147483647 it wraps around gives us a negative number, achieving integer overflow and getting our flag.
