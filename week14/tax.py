"""Tax"""
def discount(year, tax):
    """test"""
    if year < 6:
        return tax
    elif year == 6:
        return tax - (tax * 0.1)
    elif year == 7:
        return tax - (tax * 0.2)
    elif year == 8:
        return tax - (tax * 0.3)
    elif year == 9:
        return tax - (tax * 0.4)
    elif year >= 10:
        return tax - (tax * 0.5)
def main():
    """psit"""
    year = int(input())
    cc_ = int(input())
    tax = 0
    # discount = {6:0.1, 7:0.2, 8:0.3, 9:0.4}
    if cc_ <= 600:
        tax = cc_ * 0.5

    elif 600 < cc_ <= 1800:
        tax += 600 * 0.5
        tax += (cc_-600)*1.5

    elif cc_ > 1800:
        #con3
        tax += 600 * 0.5
        tax += (1800-600)*1.5
        tax += (cc_-1800)*4
    print("%.02f" %(discount(year, tax)))
main()
