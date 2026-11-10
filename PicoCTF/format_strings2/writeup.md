## This challenge makes the problem seem more complicated than it is

Luckily the fmtstr_payload() function does all the heavy lifting.
All we have to do is calculate the offset at which our data begins to be shown on the stack. After typing multiple %p we deduce the offset is 14.
The address for the ![sus] variable is hardcoded since PIE is disabled and after writing the correct hex number there we fullfill the win condition.
