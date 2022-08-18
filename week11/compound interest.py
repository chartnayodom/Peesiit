"""Compound Interest"""
def main():
    """main"""
    pv_ = int(input())
    dok = float(input())
    year = int(input())
    for _ in range(year):
        pv_ += pv_ * (dok/100)
    print("%.2f" %(pv_))
main()
