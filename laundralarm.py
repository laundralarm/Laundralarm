import RPi.GPIO as GPIO
import time
from notify_run import Notify
notify = Notify()


print("Welcome to Laundralarm!")
time.sleep(2)
print("You will now be prompted a QR code to receive texts")
time.sleep(2)

#answer = input("Would you like to proceed? yes/no ")

#if answer == yes:
   # print("Please scan the QR code and tap on the subscribe button to receive an aler when your laundry is done")
#else:
    #quit()
    
time.sleep(2)
print(notify.register()) #Prints QR Code to register channel
time.sleep(10)
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
        notify.send('Your cycle is done!') #Send notification to user 
        break 
        time.sleep(1)
        
        
        
