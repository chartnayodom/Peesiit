"""WPM"""
def main():
    """psit"""
    old = input()
    speed = int(input())
    if (old == "Kids" and speed < 11) or (old == "Adults" and speed < 26):
        print("Very Slow")
    elif (old == "Adults" and 66 <= speed <= 80) or (old == "Kids" and speed > 40):
        print("Very Fast")
    elif old == "Kids":
        if 11 <= speed <= 20:
            print("Slow")
        elif 21 <= speed <= 30:
            print("Average")
        elif 31 <= speed <= 40:
            print("Fast")
    elif old == "Adults":
        if 26 <= speed <= 35:
            print("Slow/Beginner")
        elif 36 <= speed <= 45:
            print("Intermediate/Average")
        elif 46 <= speed <= 65:
            print("Fast/Advanced")
        else:
            print("Insane")
main()
