"""Blackjack"""
def main():
    """Main FUnction"""
    hands = int(input())
    cards = ""
    for _ in range(hands):
        cards += input()
    
    ace_count = 0
    point = 0
    for char in cards:
        if char == "A":
            ace_count += 1
        elif char in "JQK":
            point += 10
        else:
            point += int(char)
    
    if ace_count == 3:
        point = 13
    elif ace_count == 2:
        if point+12 > 21:
            point += 2
        else:
            point += 12
    elif ace_count == 1:
        if point+11 > 21:
            point += 1
        else:
            point += 11
    print(point)

main()
