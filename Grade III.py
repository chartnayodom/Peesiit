"""PSIT"""
def check(number):
    if number >= 95 and number <= 100:
        return('4')
    elif number >= 90 and number < 95:
        return('3.5')
    elif number >= 85 and number < 90:
        return('3')
    elif number >= 80 and number < 85:
        return('2.5')
    elif number >= 75 and number < 80:
        return('2')
    elif number >= 70 and number < 75:
        return('1.5')
    elif number >= 65 and number < 70:
        return('1')
    elif number >= 60 and number < 65:
        return('0.5')
    elif number >= 0 and number < 60:
        return('0')
def main():
    """PSIT"""
    sub = int(input())
    num = float(input())
    sumpoint = 0
    run = 1
    while run < num:
        num1 = float(input())
        sumpoint += float(check(num1))
        # num1 = float(input())
        run += 1
        print(sumpoint)
main()
