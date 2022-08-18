"""[Midterm] Parallelogram"""
def main():
    """Main Function"""
    txt = input()
    #print("test")
    for lop in range(1, len(txt)+1):
        #print(lop, end="")
        print(txt[0:lop].rjust(len(txt)))
    for lop1 in range(len(txt)-1):
        #(1,lop1, end="")
        print(txt[lop1+1:len(txt)])
main()
