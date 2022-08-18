"""Align"""

def main():
    """main"""
    num = int(input())
    text = input()
    word = input()
    ans = num-len(word)
    if text == 'center':
        if not ans%2:
            print(word.center(num))
        else:
            print(" "*(ans//2+1)+word+" "*(ans//2))
    elif text == 'left':
        print(word.ljust(num))
    elif text == 'right':
        print(word.rjust(num))
main()
