GPIO.setup(channel, GPIO.IN)

last_callback_time = time.time()
#while GPIO.input(channel) == GPIO.RISING: #While input is in channel 17, print Nothing detected
 #   print("Nothing detected") 

#input_value = GPIO.input(17)
#print (input_value)

def callback(channel):
        last_callback_time = time.time()
        print ("Machine is running")


#if vibration isnt detected for more than 15min, then notify user.

GPIO.add_event_detect(channel, GPIO.RISING, bouncetime=50)  # let us know when the pin goes HIGH or LOW
GPIO.add_event_callback(channel, callback)  # assign function to GPIO PIN, Run function on change
# infinite loop    
while True:
    if time.time() - last_callback_time > 10:
        print("Cycle finished")
        time.sleep(1)
