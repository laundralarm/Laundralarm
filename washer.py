import RPi.GPIO as GPIO
import time
import os
from twilio.rest import Client


print("Welcome to Laundralarm! We make your life easier by notifying you when your laundry cycle is done.")
time.sleep(2)
number = input("Before we proceed, please provide your phone number: ")


account_sid = '' #hidden for privacy
auth_token = ''
client = Client(account_sid, auth_token)
time.sleep(1020) #Washer time sleep to 1020 seconds - equivalent to 19min. Last 4 minutes of the washer is the highest

print("System is starting.....")
#GPIO SETUP
channel = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(channel, GPIO.IN)

last_callback_time = time.time()



def callback(channel):
        global last_callback_time
        last_callback_time = time.time() #calls the current time 
        print ("Machine is running" )
        print(last_callback_time)
       

GPIO.add_event_detect(channel, GPIO.RISING, bouncetime=50)  # let us know when the pin goes HIGH or LOW
GPIO.add_event_callback(channel, callback)  # assign function to GPIO PIN, Run function on change

# while loop    
while True:
    if time.time() - last_callback_time > 150: #no vibration detected for 150 seconds, text user 
        message = client.messages \
                .create(
                     body="Your cycle is done!",
                     from_='+13345083288',
                     to= number
                 )#Send notification to user
        GPIO.remove_event_detect(channel)
        break 
        exit()
        
        
        
