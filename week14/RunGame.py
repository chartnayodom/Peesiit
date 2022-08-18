"""Rungame"""
def main():
    """main"""
    txt = list(input().split())
    score = 0
    for i in range(len(txt)):
        if i%2 == 0:
            score += int(txt[i])
    print(score)
main()
