from time import sleep
from threading import Thread
import tkinter as tk

def get_window():
    window = tk.Tk()

    var = tk.StringVar()
    var.set("Look Away Now")
    lbl = tk.Label(window,textvariable=var,font=("Arial",30))
    lbl.pack()

    window.geometry("400x100")

    return window

window = get_window()
window.withdraw()

class closewindow(Thread):
    def run(self):
        sleep(3)
        window.withdraw()

class blink20(Thread):
    def run(self):
        sleep(20*60)
        window.update()
        window.deiconify()
        closewindow().start()
        self.run()

blink20().start()
window.mainloop()