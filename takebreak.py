# This is a practice program called "Take A Break" written for
# Udacity course "Programming Foundations with Python"

import time
import webbrowser

print("This program encourages you to take frequent breaks throughout the work day.")
hours = input("Please input the number of hours you'll be working today: ")
print("See you in two hours.")

numberOfBreaks = hours/2

for x in xrange(0,numberOfBreaks):
    time.sleep(2*60*60)
    webbrowser.open("https://www.youtube.com/watch?v=zq7Eki5EZ8o")
