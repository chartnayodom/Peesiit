"""duplicate"""
def main():
    """Main function"""
    many_m = int(input())
    many_n = int(input())
    list_m = []
    list_n = []
    dup = []
    for _ in range(many_m):
        list_m.append(input())
    for _ in range(many_n):
        list_n.append(input())
    for i in list_m:
        for j in list_n:
            if i == j:
                dup.append(i)
            else:
                pass
    if len(dup) == 0:
        print("Nope")
    else:
        dup.sort(reverse=True)
        for loop in dup:
            print(loop)
main()
