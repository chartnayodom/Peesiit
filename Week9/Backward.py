"""backward"""
def main():
    """main"""
    pok = []
    while True:
        inp = input()
        if inp == "NULL":
            break
        else:
            pok.append(inp)
    for i in range(len(pok)-1, -1, -1):
        print(pok[i])

main()
