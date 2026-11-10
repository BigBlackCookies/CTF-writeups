## JWT challenge that covers token forging without a key

We are first presented with a login page. Our target is to become admin. With your inspector of choice we see we have a JWT assigned to our session. 

[image]

Inspecting the jwt in jwt.io we see what parameters it uses.

I tried brute forcing the key with rockyou.txt but nothing came up.
[img]

Then i remembered some website have bad config that allows making jwt tokens without signing them. Doing this I got admin privileges and got the flag.

[img]
