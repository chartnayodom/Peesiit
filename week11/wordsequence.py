"""Wordsequence"""
def main():
    """main"""
    txt1 = list(input())
    txt2 = list(input())
    txt3 = txt1
    bnk = ""
    print(bnk.join(txt3))
    for i in range(min(len(txt1), len(txt2))):
        if txt1[i] == txt2[i]:
            print(bnk.join(txt3))
        else:
            txt3[i] = txt2[i]
            print(bnk.join(txt3))
    if len(txt1) > len(txt2):
        for i in range(len(txt2), len(txt1)):
            txt3[i] = ""
            print(bnk.join(txt3))
    else:
        for i in range(len(txt1), len(txt2)):
            txt3 += txt2[i]
            print(bnk.join(txt3))
    # print(bnk.join(txt3))
main()
