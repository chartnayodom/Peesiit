"""Area"""
def main():
    """main"""
    row = int(input())
    count = 0
    for _ in range(row):
        text = input().replace(" ", "")
        count += len(text)
        # print(text)

    print(count)

main()
