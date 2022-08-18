"""Sad life of tuple"""

def main():
    """Main Function"""
    tuple_in = tuple(input())
    tuple_find = input()
    loc = tuple_in.count(tuple_find)
    ind = tuple_in.index(tuple_find)
    #print(loc)
    for _ in range(loc):
        for _ in range(loc):
            if ind <= 0:
                print(ind, end=" ")
            else:
                print(ind-1, end=" ")
        print()
main()
