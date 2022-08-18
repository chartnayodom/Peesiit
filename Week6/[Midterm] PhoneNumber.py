"""[Midterm] PhoneNumber"""
def main():
    """"[Midterm] PhoneNumber"""
    phone = input()
    country = input()
    if country == "Domestic":
        print(phone[:-8], phone[-8:-4], phone[-4:])
    elif country == "International":
        if len(phone) == 10:
            print("+66"+phone[-9:-8], phone[-8:-4], phone[-4:])
        else:
            print("+66", phone[-8:-4], phone[-4:])
main()
