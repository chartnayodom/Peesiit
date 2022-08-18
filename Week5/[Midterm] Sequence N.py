"""Sequence N"""
def main():
    """Main Function"""
    n_num = int(input())
    for i in range(n_num):
        for j in range(n_num):
            #print("*", end="")
            #สร้างเงื่อนไข
            if j == 0 or j == n_num-1:
                print("*", end="")
            elif j == i:
                print("*", end="")
            else:
                print(" ", end="")
        print()
main()
