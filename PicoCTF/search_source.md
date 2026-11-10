## Very confusing source search

We are supposed to find an artifact the developer left behind(likely the flag)

As a hint we are told to mirror the website somehow.

I first tried to download the html template for comparison but found nothing useful for my ctf
[img here]

Turns out to mirror it succesfully we have to use the tool [httrack] on the challenge instance itself.

Next thing we do is look through the pulled files using [grep -rni "picoCTF{" *] and we get the flag

[img here]
