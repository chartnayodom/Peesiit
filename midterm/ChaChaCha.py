"""Cha Cha Cha"""
def main():
    """Main Function"""
    w_day = int(input())
    income = 0
    for _ in range(w_day):
        w_hour = float(input())
        w_hour2 = int(w_hour)
        if w_hour % 1:
            w_hour2 += 1
        income += (8720 * w_hour2)
    print(int(income))
main()
