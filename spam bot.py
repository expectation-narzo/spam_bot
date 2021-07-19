import pyautogui
import time
from time import sleep
from spam_bot import spam

data = ['N','A','R','Z','O',' ','S','P','A','M',' ','B','O','T','                     ']
for x in data:
    print(x, end=''); sleep(0.2)
   
    print ("")
spammessage = input("ENTER MESSAGE:")
spamcount= input("ENTER COUNT:")

msg = spammessage
msg_count = spamcount
pyautogui.press("enter")
spam(msg, msg_count)



