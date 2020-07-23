#Remember to follow me on tiktok ;) @_r.x.t.i_

from pyhibp import pwnedpasswords as pw 
from sendsms import SMS
import json
import pyhibp
import time

pyhibp.set_user_agent(ua="blahblahblah/0.0.1 (Protecting ourselves since covid 19. BLACKLIVESMATTER)")

#load passwords
f = open("pwds.json", "r")
pwdata = json.load(f)
f.close()

while True:
	print("Checking if we've been pwned...")
    breachedpwds = []
    for password in pwdata["passwords"].values():
        resp = pw.is_password_breached(password=password)
        if resp:
            breachedpwds.append(password)

    f = open("message.txt", "w")
    f.write("The following password(s) have been compromised:\n") #feel free to personalize this message best to your needs...
    for i in breachedpwds:
        f.write(u"\u2022" + i +'\n')
    f.close()

    #if any passwords have been breached send message
    if len(breachedpwds) != 0:
        f = open("message.txt", "r")
        message = f.read()
        SMS(message)
        f.close()
	
	time.sleep(86400)                           #check every 24 hours
    
