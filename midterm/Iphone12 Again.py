"""Iphone13"""
def iphone(model, cap):
    """check iphone model"""
    if model == "iPhone 13 mini" and cap == "128 GB":
        print("25900")
    elif model == "iPhone 13 mini" and cap == "256 GB":
        print("29900")
    elif model == "iPhone 13 mini" and cap == "512 GB":
        print("37900")
    elif model == "iPhone 13" and cap == "128 GB":
        print("29900")
    elif model == "iPhone 13" and cap == "256 GB":
        print("33900")
    elif model == "iPhone 13" and cap == "512 GB":
        print("41900")
    else:
        print("Not Available")
    return 0

def iphonepro(model, cap):
    """check iphone model"""
    if model == "iPhone 13 Pro" and cap == "128 GB":
        print("38900")
    elif model == "iPhone 13 Pro" and cap == "256 GB":
        print("42900")
    elif model == "iPhone 13 Pro" and cap == "512 GB":
        print("50900")
    elif model == "iPhone 13 Pro" and cap == "1 TB":
        print("58900")
    elif model == "iPhone 13 Pro Max" and cap == "128 GB":
        print("42900")
    elif model == "iPhone 13 Pro Max" and cap == "256 GB":
        print("46900")
    elif model == "iPhone 13 Pro Max" and cap == "512 GB":
        print("54900")
    elif model == "iPhone 13 Pro Max" and cap == "1 TB":
        print("62900")
    else:
        print("Not Available")
    return 0

def main():
    """Main Function"""
    model = input()
    mem_cap = input()
    if model[7:13] == "13 Pro":
        iphonepro(model, mem_cap)
    elif model[7:9] == "13":
        iphone(model, mem_cap)
    else:
        print("Not Available")
main()
