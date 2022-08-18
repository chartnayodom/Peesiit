"""Matrix_MN"""

def main():
    """main"""
    row = int(input())
    col = int(input())
    for _ in range(row):
        lst = []
        for _ in range(col):
            lst.append(input())
        print(*lst, sep=" ")
main()