from datetime import date
import re
from Constants import RegexConstants


def IsDate(inputDate, isFinal=True, minAge=0, maxAge=100, seperator="/"):
    rValue = False
    inputDate = (inputDate or None).strip()
    re.sub(RegexConstants.AllowedSeperatorRegex, '/', inputDate)
    if (seperator != "") & (len(re.findall(RegexConstants.AllowedSeperatorRegex, seperator)) == 0):
        inputDate = inputDate.replace(seperator, "/")
    components = re.sub(RegexConstants.TrimEndRegex, '', inputDate).split('/')
    day = 0
    if len(components) > 0:
        rValue = re.match(RegexConstants.IsDigit, components[0]) is not None
        if rValue:
            day = int(components[0])
            rValue = (0 < day <= 31) or (day == 0 and len(components[0]) == 1 and len(components) == 1)
    month = 0
    if len(components) > 1 and rValue:
        maxDays = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        rValue = re.match(RegexConstants.IsDigit, components[1]) is not None
        if rValue:
            month = int(components[1])
            rValue = ((month <= len(maxDays)) and day <= maxDays[month - 1]) or (month == 0 and len(components[1]) == 1 and len(components) == 2)
    year = 0
    if rValue and len(components) > 2:
        rValue = re.match(r'^\d{1,4}$', components[2]) is not None
        if rValue:
            year = int(components[2])
            checkLeapYear = True if month == 2 and day == 29 else False
            startYear = date.today().year - maxAge
            endYear = date.today().year - minAge
            currenMonth = date.today().month
            currenday = date.today().day
            if month > currenMonth:
                endYear -= 1
            elif month < currenMonth:
                startYear -= 1
            elif day > currenday:
                endYear -= 1
            else:
                startYear -= 1
            if len(components[2]) == 1:
                rValue = (year == startYear // 1000 | year == endYear // 1000) | (
                            (startYear % 100) // 10 <= year <= (endYear % 100) // 10)
                checkLeapYear = False
            if len(components[2]) == 2:
                startCentury = startYear // 100
                endCentury = endYear // 100
                rValue = (year in range(startCentury, endCentury)) | (checkLeapYear & year == 0)
                for century in range(startCentury, endCentury):
                    rValue == startCentury <= century * 100 + year <= endCentury
                    if rValue:
                        break
            if len(components[2]) == 3:
                checkLeapYear = False
                rValue = startYear <= year*10 <= endYear
            if len(components[2]) == 4:
                rValue = startYear <= year <= endYear
            if rValue & checkLeapYear:
                if year == 0:
                    rValue = year % 400 == 0
                else:
                    rValue = year % 4 == 0
    if rValue & isFinal:
        rValue = len(components) == 3
        if rValue:
            rValue = len(components[2]) == 2 or len(components[2]) == 4
    return rValue
