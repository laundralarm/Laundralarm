import time

# User Input
typeOfDevice = input("Are you using your Washer or Dryer? ")
# User phone number
phoneNumber = input("Where would you like to receive texts? ")
# Printing out confirmation
print("You selected: " + typeOfDevice + "and your phone number is" + phoneNumber)

if typeOfDevice == "washer":
    time.sleep(5)  # wait 5 seconds
    # will add code here
    print("Timer is Done")
elif typeOfDevice == "dryer":
    time.sleep(10)  # wait 10 seconds
    # will add code here
    print("Timer is Done")
