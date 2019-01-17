# Определяет введенные данные, и их первичное сообтветствие
# если это арабское число, оно в диапазоне от 0 до 3999.
# Если это римское число оно состоит из символов:
# 'I', 'V', 'X', 'L', 'C', 'D', 'M'.
# Делается проверка римского числа на соответствие.
# Если такое римсое число не существует возвращается сообщение


def convert(s):
    if s.isdecimal():
        if int(s) > 0 and int(s) < 4000:
            return arToRom(int(s))
        else:
            koment = 'Введите число от 1 до 3999'
            return koment
    else:
        mas = ['I', 'V', 'X', 'L', 'C', 'D', 'M']
        for i in s:
            if i in mas:
                pass
            else:
                koment = 'Это не римское число'
                return koment
        tempRom = romToAr(s)
        reversConvert = arToRom(tempRom)
        if s == reversConvert:
            return tempRom
        else:
            return 'несуществующее римсоке число'


# Конвертирует арабское число в римское


def arToRom(data):
    ones = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]
    tens = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
    hunds = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
    thous = ["", "M", "MM", "MMM", "MMMM"]
    t = thous[data // 1000]
    h = hunds[data // 100 % 10]
    te = tens[data // 10 % 10]
    o = ones[data % 10]
    return t+h+te+o


# Конвертирует римское число в арабское.


def romToAr(s):
    masRim = list(s)
    tempMasAr = []
    for i in masRim:
        if i == 'I':
            tempMasAr.append(1)
        elif i == 'V':
            tempMasAr.append(5)
        elif i == 'X':
            tempMasAr.append(10)
        elif i == 'L':
            tempMasAr.append(50)
        elif i == 'C':
            tempMasAr.append(100)
        elif i == 'D':
            tempMasAr.append(500)
        elif i == 'M':
            tempMasAr.append(1000)
    tempAr = 0
    j = 0
    while j < len(tempMasAr):
        if j == (len(tempMasAr) - 1):
            tempAr += tempMasAr[j]
            j += 1
        elif tempMasAr[j] >= tempMasAr[j + 1]:
            tempAr += tempMasAr[j]
            j += 1
        else:
            tempAr = tempAr + tempMasAr[j + 1] - tempMasAr[j]
            j += 2
    return tempAr
