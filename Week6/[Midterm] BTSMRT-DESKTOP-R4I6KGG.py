"""[Midterm] BTSMRT"""
def main():
    """"[Midterm] BTSMRT"""
    daytype = input().lower()
    age = float(input())
    height = float(input())
    if (age < 14 and height < 90) or (age < 14 and height <= 140 and daytype == 'children day')\
        or (age >= 60 and daytype == 'senior day'):
        print("FREE")
    else:
        print("PAY")
main()
