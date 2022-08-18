"""inflation"""
def main():
    """Main Function"""
    money = float(input())
    year = int(input())
    for _ in range(year):
        money += money * 0.0381
    money = int(money*100)
    print("%.2f" %(money/100))
main()