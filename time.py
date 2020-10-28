
import time

#User Input 
type = input("Are you using your Washer or Dryer? ")
#User phone number
phonenumber = input("Where would you like to receive texts? ")
#Printing out confirmation
print("You selected: " + type + "and your phone number is" + phonenumber)

if type == "washer":
    time.sleep(5) #wait 5 seconds
    #will add code here
    print("Timer is Done")
elif type == "dryer":
    time.sleep(10) #wait 10 seconds
    #will add code here
    print("Timer is Done")

