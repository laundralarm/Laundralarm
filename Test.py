import RPi.GPIO as GPIO
import time


#User Input 
type = input("Are you using your Washer or Dryer? ")
#User phone number
phonenumber = input("Where would you like to receive texts? ")
#Printing out confirmation
print("You selected: " + type + "and your phone number is " + phonenumber)

#GPIO SETUP
channel = 17 #Where the input is connected to
GPIO.setmode(GPIO.BCM)
GPIO.setup(channel, GPIO.IN)

if type == "washer":
    def callback(channel):
        print("Vibration Detected!") #This will keep printing if movement detected
    #time.sleep(10)
    #print("Timer is Done") #This should print when there is no vibration detected
elif type == "dryer":
    def callback(channel):
        print("Vibration Detected!")
    #time.sleep(10)
    #print("Timer is Done") #This should print when there is no vibration detected

    
GPIO.add_event_detect(channel, GPIO.RISING, bouncetime=100)  # let us know when the pin goes HIGH or LOW
GPIO.add_event_callback(channel, callback)  # assign function to GPIO PIN, Run function on change
# infinite loop
while True:
        time.sleep(1)
        
        
        


