"""Bill"""

def main():
    """main"""
    num = int(input())
    ser = ((num*10)/100)
    if 50 <= ser <= 1000:
        num += ser
    elif ser < 50:
        num += 50
    elif ser > 1000:
        num += 1000
    vat = num*0.07
    total = num+vat
    print("%.2f" %(total))
main()
