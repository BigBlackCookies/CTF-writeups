### **EASY-HIDE WRITEUP**

simple steganography problem

<span style="color:red">NOTE TO SELF GET MORE COMFORTABLE TO MODIFYING BYTES OF A IMAGE WITH HxD</span>

- After binwalking the given jpg inside there is another jpg that refuses to open but ahs jpg extension
- inspecting the extracted jpg in a hex editor we can see the magic(first) bytes are wrong and we modify them to the right ones for a jpg file
- flag is in the photo good job well done