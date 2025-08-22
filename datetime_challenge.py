from datetime import datetime
import pytz

# Set the timezones
NewYork_tz = pytz.timezone('America/New_York')
Portland_tz = pytz.timezone('America/Los_Angeles')
London_tz = pytz.timezone('Europe/London')

# Get current time in timezone
current_time = datetime.now().strftime("%H:%M")
current_minute = datetime.now().strftime("%M")
timein_NewYork = datetime.now(NewYork_tz).strftime("%H:%M")
hourin_NewYork = int(datetime.now(NewYork_tz).strftime("%H"))
timein_Portland = datetime.now(Portland_tz).strftime("%H:%M")
hourin_Portland = int(datetime.now(Portland_tz).strftime("%H"))
timein_London = datetime.now(London_tz).strftime("%H:%M")
hourin_London = int(datetime.now(London_tz).strftime("%H"))

openClosed = {"New York":hourin_NewYork,"Portland":hourin_Portland,"London":hourin_London}
time = {"New York":timein_NewYork,"Portland":timein_Portland,"London":timein_London}

print("All branches are open from 09:00 - 17:00\nLocal time is: {}\n".format(current_time))
for key in openClosed:
    value = openClosed[key]
    if value > 9 and value < 17:
        print("The current time in {} is {}:{}. Therefore the branch is open.".format(key,value,current_minute))
    else:
        print("The current time in {} is {}:{}. Therefore the branch is closed.".format(key,value,current_minute))
