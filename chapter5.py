## Exercise 5.1.
# Converts it to a time of day in hours, minutes, and seconds, plus the number of days since the epoch.

import time

# the epoch time
epoch = int(time.time())

# calculate number of days since epoch
days = epoch / (60 * 60 * 24)
hour = days % int(days) * 24
min  = hour % int(hour) * 60
sec  = min % int(min) * 60

print(f"Days since epoch: {int(days)}\nCurrent Time: {int(hour)}:{int(min)}:{int(sec)}")

## Exercise 5.2.
