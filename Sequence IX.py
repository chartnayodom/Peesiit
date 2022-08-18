"""Sequence IX"""
def main():
    """Main Function"""
    num = int(input())
    for i in range(1, num+1):
        print("   " * (num-i), end="")
        for j in range(1, i+1):
            print("%02d" %j, end=" ")
        for k in range(j-1, 0, -1):
            print("%02d" %k, end=" ")
        print()
main()
