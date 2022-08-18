"""Progessive Tax"""
def k150(income):
    """saddas"""
    if income > 300000:
        diff = (150000 * 100) * 5 // 10000
    else:
        diff = ((income - 150000)*100) * 5 // 10000
    return diff
def k300(income):
    """saddas"""
    if income > 500000:
        diff = (200000 * 100) * 10 // 10000
    else:
        diff = ((income - 300000)*100) * 10 // 10000
    return diff
def k500(income):
    """saddas"""
    if income > 7500000:
        diff = (250000 * 100) * 15 // 10000
    else:
        diff = ((income - 500000)*100) * 15 // 10000
    return diff
def k750(income):
    """saddas"""
    if income > 1000000:
        diff = (250000 * 100) * 20 // 10000
    else:
        diff = ((income - 750000)*100) * 20 // 10000
    return diff
def m01(income):
    """saddas"""
    if income > 2000000:
        diff = (1000000 * 100) * 25 // 10000
    else:
        diff = ((income - 1000000)*100) * 25 // 10000
    return diff
def m02(income):
    """saddas"""
    if income > 4000000:
        diff = (2000000 * 100) * 30 // 10000
    else:
        diff = ((income - 2000000)*100) * 30 // 10000
    return diff
def m04(income):
    """saddas"""
    diff = ((income - 4000000)*100) * 35 // 10000
    return diff
def main():
    """Main function"""
    income = int(input())
    if income > 4000000:
        print(m04(income) + m02(income) + m01(income) + k750(income)\
           + k500(income) + k300(income) + k150(income))
    elif 2000000 < income <= 4000000:
        print(m02(income) + m01(income) + k750(income)\
           + k500(income) + k300(income) + k150(income))
    elif 1000000 < income <= 2000000:
        print(m01(income) + k750(income)\
           + k500(income) + k300(income) + k150(income))
    elif 750000 < income <= 1000000:
        print(k750(income)\
           + k500(income) + k300(income) + k150(income))
    elif 500000 < income <= 750000:
        print(k500(income) + k300(income) + k150(income))
    elif 300000 < income <= 500000:
        print(k300(income) + k150(income))
    elif 150000 < income <= 300000:
        print(k150(income))
    elif income <= 150000:
        print(0)
main()
