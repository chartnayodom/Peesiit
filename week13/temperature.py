"""temperature"""
def celsius(temp):
    """Give Celsius"""
    tempwant = input().upper()
    ans = 0
    if tempwant == "F":
        ans = temp*(9/5)+32
    elif tempwant == "K":
        ans = temp + 273.15
    elif tempwant == "R":
        ans = (temp + 273.15)*(9/5)
    return ans   
def fahrenheit(temp):
    """Give Fahrenheit"""
    tempwant = input().upper()
    ans = 0
    if tempwant == "C":
        ans = (temp-32)*(5/9)
    elif tempwant == "K":
        ans = ((temp-32)*(5/9))+273.15
    elif tempwant == "R":
        ans = (((temp-32)*(5/9))+273.15)*(9/5)
    return ans
def kelvin(temp):
    """Give Kelvin"""
    tempwant = input().upper()
    ans = 0
    if tempwant == "C":
        ans = temp-273.15
    elif tempwant == "F":
        ans = (temp-273.15)*(9/5)+32
    elif tempwant == "R":
        ans = temp*(9/5)
    return ans
def rankine(temp):
    """Give Rankine"""
    tempwant = input().upper()
    ans = 0
    if tempwant == "C":
        ans = (temp*(5/9)-273.15)
    elif tempwant == "F":
        ans = (temp*(5/9)-273.15)*(9/5)+32
    elif tempwant == "K":
        ans = temp*(5/9)
    return ans
def main():
    """Find Temperature"""
    number = float(input())
    temp = input().upper()
    if temp == "C":
        print("%.2f" %(celsius(number)))
    elif temp == "K":
        print("%.2f" %(kelvin(number)))
    elif temp == "F":
        print("%.2f" %(fahrenheit(number)))
    elif temp == "R":
        print("%.2f" %(rankine(number)))

main()