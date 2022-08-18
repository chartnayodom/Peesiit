"""BloodDonation"""
def main():
    """BloodDonation"""
    age = int(input())
    weight = int(input())
    donate = int(input())
    require = False
    if age < 17 or age > 70:
        print("No")
        return
    if age == 17 or 60 <= age <= 70:
        require = True
        consent = input()
    denied = weight < 45 or (age > 55 and donate == 0) or (require and consent == "False")
    if denied:
        print("No")
    else:
        print("Yes")

main()
