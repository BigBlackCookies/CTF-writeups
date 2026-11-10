## This took longer than it should've

If we closely inspect the source code we see that the binary already loads the flag on the stack we just have to bruteforce where. Using the python script that opens and closes the binary and looks for the flag by sending payloads in the format of %(counter)$s we are able to solve the challenge.
