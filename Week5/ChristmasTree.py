"""Christmas Tree"""
def main():
    """Main Function"""
    leaf = int(input())
    wood = int(input())
    for i in range(leaf):
        print(" " * (leaf-i-1), end="")
        print("*" * ((2*i)+1))#ใบไม้
    for j in range(wood):
        print(" " *(leaf-2), end="")
        print("-" * 3)
main()
