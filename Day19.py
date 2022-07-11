import datetime
import calendar
def findDay(date):
    B = datetime.datetime.strptime(date, "%d %m %Y").weekday()
    return (calendar.day_name[B])

date = '09 10 2022'
print(findDay(date))