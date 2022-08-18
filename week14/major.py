"""Area"""
def main():
    """main"""
    candi = int(input())
    people = int(input())
    score = []
    for _ in range(candi):
        score.append(0)
    print(score)
    for _ in range(people):
        choose = int(input())
        score[choose-1] += 1
    print(score)
main()