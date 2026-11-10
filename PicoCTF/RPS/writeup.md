## Cheating rock paper scissors

The binary checks what you picked and compares it using [strstr()]. The binary chooses its option by using [random()] with [srand(time(0))] which is the current time in seconds making it impossible to guess what its going to pick in advance. But since its using [strstr()] if we input all three option like [rockpaperscissors] it will be flagged as correct nonetheless. By sending this input 5 times we get the flag.
