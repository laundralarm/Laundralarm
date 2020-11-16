import RPi.GPIO as GPIO
import time
import os
from twilio.rest import Client


print("Welcome to Laundralarm! We make your life easier by notifying you when your laundry cycle is done.")
time.sleep(2)
number = input("Before we proceed, please provide your phone number: ")


account_sid = '' #left blank for privacy
auth_token = '' #left blank for privacy
client = Client(account_sid, auth_token)


print("System is starting.....")
#GPIO SETUP
channel = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(channel, GPIO.IN)

last_callback_time = time.time()
callback_called = False


def callback(channel):
        callback_called = True
        last_callback_time = time.time()
        print ("Machine is running" )
        print(last_callback_time)
       

GPIO.add_event_detect(channel, GPIO.RISING, bouncetime=50)  # let us know when the pin goes HIGH or LOW
GPIO.add_event_callback(channel, callback)  # assign function to GPIO PIN, Run function on change

# while loop    
while True:
    if time.time() - last_callback_time > 5 and callback_called == True:#If no vibration is detected for 5 sec, print CYCLE FINISHED
        callback_called = False 
        message = client.messages \
                .create(
                     body="Your cycle is done!",
                     from_='+13345083288',
                     to= number
                 )#Send notification to user 
        break 
        exit()
        
        
        
