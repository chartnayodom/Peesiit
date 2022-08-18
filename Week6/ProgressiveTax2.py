"""Progessive Tax"""
def main():
    """main"""
    income = int(input())
    tax = 0
    if income > 4000000:
        tax += (income - 4000000)*0.35
        income -= (income-4000000)
    if income > 2000000:
        tax += (income - 2000000)*0.30
        income -= (income-2000000)
    if income > 1000000:
        tax += (income - 1000000)*0.25
        income -= (income-1000000)
    if income > 750000:
        tax += (income - 750000)*0.20
        income -= (income-750000)
    if income > 500000:
        tax += (income - 500000)*0.15
        income -= (income-500000)
    if income > 300000:
        tax += (income - 300000)*0.10
        income -= (income-300000)
    if income > 150000:
        tax += (income - 150000)*0.05
        income -= (income-150000)

    print(int(tax))
main()
