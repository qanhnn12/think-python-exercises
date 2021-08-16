## Exercise 5.1 - Converts it to a time of day in hours, minutes, and seconds, plus the number of days since the epoch.

import time
total_secs = time.time()

# seconds = the remainder of total seconds divided by the number of seconds in a minute 
# minutes = the remainder of total minutes divided by the number of minutes in an hour
# the same applies for hours and days

seconds = int(total_secs % 60)
minutes = int((total_secs // 60) % 60)
hours = int((total_secs // 3600) % 24)
days = int(total_secs // (3600 * 24))

print("There have been " + str(days) +" days, " + str(hours) + " hours, " + str(minutes) + " minutes, and " + str(seconds) + " seconds since epoch.")


## Exercise 5.2.
