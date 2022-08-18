"""Diamond"""
def main():
    """Main function"""
    john = int(input())
    for i in range(john//2):
        for j in range(john):
            if j == john // 2 - i or j == john // 2 + i:
                print("*", end="")
            else:
                print(" ", end="")
        print()
    print("*" * john)
    for poo in range(1, john//2+1):
        for qoo in range(john):
            if qoo == poo or qoo == john - poo -1:
                print("*", end="")
            else:
                print(" ", end="")
        print()

main()
