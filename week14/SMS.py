"""SMS"""
def main():
    """main"""
    char = int(input())
    but2 = ['C', 'A', 'B']
    but3 = ['F', 'D', 'E']
    but4 = ['I', 'G', 'H']
    but5 = ['L', 'J', 'K']
    but6 = ['O', 'M', 'N']
    but7 = ['S', 'P', 'Q', 'R']
    but8 = ['V', 'T', 'U']
    but9 = ['Z', 'W', 'X', 'Y']
    txt = []
    for _ in range(char):
        button = int(input())
        time = int(input())
        if button == 1:
            for _ in range(time):
                if len(txt) <= 0:
                    pass
                else:
                    txt.pop()
            #del string
        elif button == 2:
            txt += but2[time % len(but2)]
        elif button == 3:
            txt += but3[time % len(but3)]
        elif button == 4:
            txt += but4[time % len(but4)]
        elif button == 5:
            txt += but5[time % len(but5)]
        elif button == 6:
            txt += but6[time % len(but6)]
        elif button == 7:
            txt += but7[time % len(but7)]
        elif button == 8:
            txt += but8[time % len(but8)]
        elif button == 9:
            txt += but9[time % len(but9)]

    if len(txt) <= 0:
        print("null")
    else:
        print("".join(txt))
main()
