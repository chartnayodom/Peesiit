"""[Midterm] BTSMRT"""
def main():
    """"[Midterm] BTSMRT"""
    daytype = input()
    age = float(input())
    height = float(input())

    if age < 14:
        if height <= 90:
            print("FREE")
        elif height <= 140:
            if daytype == "Children Day":
                print("FREE")
            else:
                print("PAY")
    elif age >= 60 and daytype == 'Senior Day':
        print("FREE")
    elif age >= 60 and daytype != 'Senior Day':
        print("PAY") # ลั่น
    else:
        print("PAY")

main()
