"""BloodDonation"""
def kid(): #Age 17 < 18
    """BloodDonation"""
    weight = int(input())
    time = int(input())
    time = time
    cert = input()
    state = True
    if weight < 45:
        state = False
    if cert == "False":
        state = False
    if state == False:
        print("No")
    else:
        print("Yes")

def adult(age): #Age 18-59
    """BloodDonation"""
    weight = int(input())
    time = int(input())
    state = True
    if weight < 45:
        state = False
    if time < 1 and age >= 55:
        state = False
    if state == False:
        print("No")
    else:
        print("Yes")

def elder(): #Age 60-70
    """BloodDonation"""
    weight = int(input())
    time = int(input())
    cert = input()
    state = True
    if weight < 45:
        state = False
    if time < 1:
        state = False
    if cert == "False":
        state = False
    if state == False:
        print("No")
    else:
        print("Yes")

def main():
    """BloodDonation"""
    age = int(input())
    if 17 <= age < 18:
        kid()
    elif 18 <= age < 60:
        adult(age)
    elif 60 <= age <= 70:
        elder()
    else:
        print("No")
main()
