"""Pick them again"""
def main():
    """Main"""
    qwe = input().split()
    ewq = []
    for i in range(len(qwe)-1, -1, -1):
        if int(qwe[i]) % 3 == 0 or int(qwe[i]) % 5 == 0:
            ewq.append(int(qwe[i]))
    if len(ewq) == 0:
        print("Nope")
    else:
        for i in ewq:
            print(i)

main()
