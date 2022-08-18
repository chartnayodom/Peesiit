"""[Midterm] Parallelogram"""
def main():
    """Main Function"""
    txt = input()
    for lop in range(len(txt) + 1): 
        print(txt[0:lop].rjust(len(txt)))
    for lop1 in range(1, len(txt) + 1): 
        print(txt[lop1:len(txt)])
main()
