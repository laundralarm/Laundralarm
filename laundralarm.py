import RPi.GPIO as GPIO
import time
import os
from twilio.rest import Client


print("Welcome to Laundralarm!")
time.sleep(2)

account_sid = 'AC789b7a1c670bad86371d94606b55c77a'
auth_token = '8cb62de772776e509246f67ee09c9da9'
client = Client(account_sid, auth_token)


print("System is starting.....")
#GPIO SETUP
channel = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(channel, GPIO.IN)

last_callback_time = time.time()


def callback(channel):
        last_callback_time = time.time()
        print ("Machine is running")
       

GPIO.add_event_detect(channel, GPIO.RISING, bouncetime=50)  # let us know when the pin goes HIGH or LOW
GPIO.add_event_callback(channel, callback)  # assign function to GPIO PIN, Run function on change

# while loop    
while True:
    if time.time() - last_callback_time > 20: #If no vibration is detected for 10 sec, print CYCLE FINISHED
        message = client.messages \
                .create(
                     body="Your cycle is done!",
                     from_='+13345083288',
                     to='+13478605680'
                 )#Send notification to user 
        break 
        time.sleep(1)
        
        
        
