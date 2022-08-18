"""[Midterm] BigFrame"""
def main():
    """[Midterm] BigFrame"""
    txt1 = input().strip()
    txt2 = input().strip()
    txt3 = input().strip()
    txt4 = input().strip()
    txt5 = input().strip()
    length = max(len(txt1), len(txt2), len(txt3), len(txt4), len(txt5))
    print("*" *(length+4))
    print("* " + txt1.ljust(length) + " *")
    print("* " + txt2.ljust(length) + " *")
    print("* " + txt3.ljust(length) + " *")
    print("* " + txt4.ljust(length) + " *")
    print("* " + txt5.ljust(length) + " *")
    print("*" *(length+4))

main()
