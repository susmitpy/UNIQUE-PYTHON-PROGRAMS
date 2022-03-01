from time import sleep
import os
from threading import Thread


class fiveMinuteBreak(Thread):
    def run(self):
        sleep(60*60)
        os.system('say "Take a 5 minute break"')
        print("After one hour")
        self.run()


class blink10(Thread):
    counter = 0

    def run(self):
        sleep(60*20)
        self.counter += 1
        if self.counter == 3:
            self.counter = 0
            self.run()
        else:
            os.system('say "Look away and blink"')
            sleep(20)
            os.system('say "Close your eyes and take a deep breath"')
            print("After 20 minutes")
            self.run()


print("Started...")
os.system('say "Started"')

fiveMinuteBreak().start()
blink10().start()


"""
Instead of os.system('say "text to speak"') , 
you can use tkinter to show window. (checkout eye_tkinter.py)
For linux, use spd-say
"""

"""
To launch at startup for OSX

#!/bin/sh
python3 {full path}/timer.py

Place the above text in a file named as eye
In System Preferences, Users and groups, Login items, add this unix executable.

"""
