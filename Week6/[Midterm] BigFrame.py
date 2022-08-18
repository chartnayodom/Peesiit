"""[Midterm] BigFrame"""
def main():
    """[Midterm] BigFrame"""
    txt1 = input()
    txt2 = input()
    txt3 = input()
    txt4 = input()
    txt5 = input()
    # txt1 = txt1.replace(" ","")
    # txt2 = txt2.replace(" ","")
    # txt3 = txt3.replace(" ","")
    # txt4 = txt4.replace(" ","")
    # txt5 = txt5.replace(" ","")
    length = max(len(txt1), len(txt2), len(txt3), len(txt4), len(txt5))
    #print(length)
    
    print("*" *(length+4))
    print("* " + txt1.ljust(length) + " *")
    print("* " + txt2.ljust(length) + " *")
    print("* " + txt3.ljust(length) + " *")
    print("* " + txt4.ljust(length) + " *")
    print("* " + txt5.ljust(length) + " *")
    print("*" *(length+4))
    
#     for i in range(8):
#         if i == 0 or i == length-1:
#             print("*" *(length+4))
#         else:
#             print(txt)
main()
ลองทำข้อRight ARROWดู

