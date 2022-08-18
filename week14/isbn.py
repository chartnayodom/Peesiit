"""ISBN"""


def main():
    """main func"""
    isbn = input().split("-")
    isbn2 = "".join(isbn)
    multi = 10
    sam = 0
    for i in range(0, len(isbn2)-1):
        sam += multi * int(isbn2[i])
        multi -= 1
    ans = (sam * -1) % 11
    if ans == 10:
        ans = "X"
    if str(ans) == isbn2[-1]:
        print("Yes")
    else:
        print("No %s" % str(ans))


main()