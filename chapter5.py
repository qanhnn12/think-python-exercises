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


## Exercise 5.2 - Check the Fermat’s Last Theorem

def check_format(a, b, c, n):
    if n > 2 and a**n + b**n == c**n:
        print("Holy smokes, Fermat was wrong!")
    else:
        print("No, that doesn't work.")

def input_num():
    a = int(input("Choose a number for a: "))
    b = int(input("Choose a number for b: "))
    c = int(input("Choose c number for c: "))
    n = int(input("Choose a number for n: "))
    return check_format(a, b, c, n)

input_num()

