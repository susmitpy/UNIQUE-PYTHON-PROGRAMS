import datetime
import calendar
while True:
    day, month, year = input("Enter the date in dd/mm/yyyy form: ").split("/")
    print(calendar.day_name[datetime.datetime(int(year), int(month), int(day)).weekday()])
