"""Difference"""
def main():
    """Main function"""
    set_a = set()
    set_b = set()
    many_a = int(input())
    many_b = int(input())
    for _ in range(many_a):
        set_a.add(int(input()))
    for _ in range(many_b):
        set_b.add(int(input()))
    # print(set_a)
    # print(set_b)
    a_b = set_a
    for i in set_b:
        a_b.discard(i)
    ans = sorted(a_b)
    for loop in ans:
        print(loop, end=" ")
main()
