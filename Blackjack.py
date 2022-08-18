"""Pre Blackjack"""
def main():
    """Main Function"""
    p_card = int(input())
    point = 0
    ace_counter = 0
    for _ in range(p_card):
        chk = input()
        if chk.isnumeric() == 1:
            point += int(chk)
            # if int(chk) >= 2 and int(chk) <= 10:
            #     point += int(chk)
            # else:
            #     point += 0
        elif chk == "J" or chk == "K" or chk == "Q":
            point += 10
        elif chk == "A":
            ace_counter += 1

    if ace_counter == 3:
        point = 13
    elif ace_counter == 2:
        if point+12 > 21:
            point += 2
        else:
            point += 12
    elif ace_counter == 1:
        if point+11 > 21:
            point += 1
        else:
            point += 11
    print(point)

main()
