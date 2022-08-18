"""inflation"""
def main():
    """Main Function"""
    money = float(input())
    money = int(money*100)
    year = int(input())
    for _ in range(year):
        money += money*381//10000
    print("%d.%02d" %(money//100, money%100))
main()
