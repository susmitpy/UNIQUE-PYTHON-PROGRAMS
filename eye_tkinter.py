from time import sleep
from threading import Thread
import tkinter as tk
import os


class App(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.label = tk.Label(self, text="Look away now", font=("Arial", 30))
        self.label.pack()
        self.geometry("400x100")

    def set_look_away_text(self):
        self.label["text"] = "Look away now"

    def set_break_text(self):
        self.label["text"] = "Take a 5 minute break"


window = App()


class closewindow(Thread):
    def run(self):
        sleep(3)
        window.withdraw()


class fiveMinuteBreak(Thread):
    def run(self):
        sleep(60 * 60)
        os.system('spd-say "Take a 5 minute break"')
        window.set_break_text()
        window.update()
        window.deiconify()
        closewindow().start()
        self.run()


class blink20(Thread):
    counter = 0

    def run(self):
        sleep(20 * 60)
        self.counter += 1
        if self.counter == 3:
            self.counter = 0
            self.run()
        else:
            window.set_look_away_text()
            window.update()
            window.deiconify()
            closewindow().start()
            os.system("spd-say 'Look Away Now'")
            self.run()


os.system("spd-say Started")
fiveMinuteBreak().start()
blink20().start()
window.mainloop()
