from datetime import datetime,timedelta
import time
x = datetime.now() #when the deal is accepted
y = x + timedelta(days=30)
z = y - x

def countdown(z):
    while True:
        diff = z - datetime.now()
        count_hours , rem = divmod(diff.seconds, 3600)
        count_minutes, count_seconds = divmod(rem,60)
        if diff.days == 0 and count_minutes == 0 and count_seconds == 0 and count_hours == 0:
            # call the required function when the loop is com[plteted
            print("Time's up..!")
            break
        print('The count is: '
              + str(diff.days) + " day(s) "
              + str(count_hours) + " hour(s) "
              + str(count_minutes) + " minute(s) "
              + str(count_seconds) + " second(s) "
              )
        time.sleep(1)

print("Current Date and Time: ", x)
print("Final Date and Time of payment: ",y)
print("time difference: ",str(z))
countdown(y)