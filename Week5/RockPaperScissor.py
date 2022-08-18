"""RockPaperScissor"""
def main():
    """Main function"""
    play = input()
    p_a = 0
    p_b = 0
    for lop in range(0, len(play), 2):
        paa = play[lop]
        pab = play[lop+1]
        if paa == "R" and pab == "S":
            p_a += 1
        elif paa == "P" and pab == "R":
            p_a += 1
        elif paa == "S" and pab == "P":
            p_a += 1
        elif paa == "R" and pab == "P":
            p_b += 1
        elif paa == "P" and pab == "S":
            p_b += 1
        elif paa == "S" and pab == "R":
            p_b += 1
        elif paa == pab:
            continue

    if p_a > p_b:
        print("A win %d-%d" %(p_a, p_b))
    if p_a < p_b:
        print("B win %d-%d" %(p_b, p_a))
    if p_a == p_b:
        print("DRAW %d" %p_a)

main()
