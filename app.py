import pywhatkit as kit
import time

# Wait for repl.it to start properly
time.sleep(10)

# Send message instantly
kit.sendwhatmsg_instantly(
    "+919996207896",   # receiver's number
    "Hello! This is my bot running on Replit 🚀",
    20,  # tab_close after 40 sec
    True, # close tab
    3     # wait time
)

print("Message sent!")
