import datetime
import calendar
def findDay(date):
    B = datetime.datetime.strptime(date, "%d %m %Y").weekday()
    return (calendar.day_name[B])

    if month == 'december':
        sign = 'sagittarius' if (day < 22 ) else 'capricorn'
    elif month == 'january':
        sign = 'capricorn' if (day <20) else 'aquarius'
    elif month == 'february':
        sign = 'aquarius' if (day <20) else 'pisces'
    elif month == 'march':
        sign = 'pisces' if (day <20) else 'aries'
    elif month == 'april':
        sign = 'aries' if (day <20) else 'taurus'
    elif month == 'may':
        sign = 'taurus' if (day <20) else 'gemini'
    elif month == 'june':
        sign = 'gemini' if (day <20) else 'cancer'
    elif month == 'july':
        sign = 'cancer' if (day <20) else 'leo'
    elif month == 'august':
        sign = 'leo' if (day <20) else 'virgo'
    elif month == 'september':
        sign = 'virgo' if (day <20) else 'libra'
    elif month == 'october':
        sign = 'libra' if (day <20) else 'scorpio'
    elif month == 'november':
        sign = 'scorpio' if (day <20) else 'sagittarius'

print(findDay('09 10 2022'))