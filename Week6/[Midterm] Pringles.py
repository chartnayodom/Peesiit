"""[Midterm] Pringles"""
def main():
    """Main Function"""
    line1 = input()
    line2 = input()
    line3 = input()
    eat = int(input())
    eaten = 0
    newline2 = ""
    for i in range(eat):
        if line2[i] == ')':
            newline2 += " "
            eaten += 1
        else:
            newline2 += " "
    for j in range(len(newline2), len(line2)):
        newline2 += line2[j]
    print(eaten)
    #print(newline2.find(')'))
    if newline2.find(')') > 0:
        print("There are still some left.")
    else:
        print("None.")
    print(line1)
    print(newline2)
    print(line3)

main()
