import re

import Constants.RegexConstants


def Int(inputString):
    rValue = re.match(r'^\d*$', inputString) is not None
    a = inputString if rValue else ""
    return rValue, a


def Decimal(inputString):
    rValue = re.match(r'^\d*((\.)\d*)?$', inputString) is not None
    a = inputString if rValue else ""
    return rValue, a


def Double(inputString):
    rValue = re.match(r'^\d*((\.)\d{1,2})?$', inputString) is not None
    a = inputString if rValue else ""
    return rValue, a
