"""Future Message"""
def main():
    """Main Function"""
    txt = input()
    if txt.isnumeric():
        print("Number")
    elif txt.isupper():
        print("Uppercase")
    elif txt.islower():
        print("Lowercase")
    elif txt.istitle():
        print("Title")
    elif txt.isspace():
        print("Space")
    else:
        print("Other")
main()
