import RPi.GPIO as GPIO
import time

# GPIO SETUP

channel = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(channel, GPIO.IN)

last_callback_time = time.time()


def callback(channelIn):
    last_callback_time = time.time()
    print("Movement Detected!")


# Perhaps do: GPIO.RISING instead of BOTH.
GPIO.add_event_detect(channel, GPIO.BOTH, bouncetime=300)  # let us know when the pin goes HIGH or LOW
GPIO.add_event_callback(channel, callback)  # assign function to GPIO PIN, Run function on change
# infinite loop
while True:
    if time.time() - last_callback_time  > 300:
        # send notificaiton
    time.sleep(1)
