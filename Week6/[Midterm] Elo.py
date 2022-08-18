"""[Midterm] Elo"""
def main():
    """Main Function"""
    rate_a = int(input())
    rate_b = int(input())
    choose = input().lower()
    if choose == 'a':
        print("%.02f" %(1 / (1 + (10 ** ((rate_b - rate_a)/400)))))
    if choose == 'b':
        print("%.02f" %(1 / (1 + (10 ** ((rate_a - rate_b)/400)))))
main()
