#
# Example of how to get an output after five seconds of inactivity.
#
import time

last_callback_time = time.time()  # Initialize the last time we had a vibration.
waiting_time = time.time()  # Initialize the timer for waiting.
seconds_to_count_down = 3   # How long we want to wait before our five second countdown.
keep_looping = True         # Use a boolean for the while condition.


def callback(channel):
    return time.time()


while keep_looping:
    # We first count down for `seconds_to_count_down` seconds,
    # updating our last_callback_time time.
    if time.time() - waiting_time < seconds_to_count_down:
        last_callback_time = callback(17)
        print(time.time() - last_callback_time)
    # Once last_callback_time is no longer being updated,
    # and we've waited for five seconds, this will print
    # the message and stop the loop.
    if time.time() - last_callback_time > 5:
        print("No input for several seconds!")
        keep_looping = False

