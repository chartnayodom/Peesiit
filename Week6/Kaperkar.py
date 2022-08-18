"""Karprekar"""
def main():
    """Main function"""
    num = int(input())
    time = 0
    nam = str(num)
    while True:
        # print("start")
        # print(nam)
        # print(type(nam))
        time += 1
        num1 = ""
        num2 = ""
        for i in range(9, -1, -1):
            if nam.count(str(i)):
                num1 += str(i) * nam.count(str(i))
        for j in range(0, 10):
            if nam.count(str(j)):
                num2 += str(j) * nam.count(str(j))
        if len(num1) < 4:
            num1 += "0"
        # print(num1, num2)
        # print("continue")
        nam = int(num1) - int(num2)
        if nam == 6174:
            break
        elif nam < 1000:
            nam *= 10
            nam = str(nam)
        else:
            nam = str(nam)
    print(time)
main()
