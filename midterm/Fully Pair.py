"""Fully Pair"""
def main():
    """main"""
    txt = input()
    txt2 = txt
    txt3 = ""
    for chk in txt2:
        pip = txt2.count(chk) % 2
        txt2 = txt2.replace(chk, "")
        txt3 += chk * pip
    if len(txt3) == 0:
        print("fully paired")
    else:
        print(txt3)

main()
