import time, datetime
start = time.time()
a = input("Stopwatch Started \nPress Any Key To Stop\n")
print(datetime.datetime.fromtimestamp(time.time()) - datetime.datetime.fromtimestamp(start)) #datetime object - datetime object
input() # To prevent the closing of console
