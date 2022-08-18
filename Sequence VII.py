"""Sequence VII"""
def main():
    """Main FUnction"""
    num = int(input())
    numi = 0
    txt = ''
    for i in range(num):
        for j in range(i+1):
            print(j+1, end=" ")
        print()
    for i in range(num-1):
        for j in range(num-(i+1)):
            print(j+1, end=" ")
        print()
main()
