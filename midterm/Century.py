"""Century"""
def check(data):
    """YEP"""
    if data[:4] == "B.E." or data[:4] == "A.D.":
        pass
    else:
        print("ERROR")
        return
    year = int(data[5:])
    if data[0] == 'B':
        year -= 543

    if year <= 0:
        print("ERROR")
        return
    cent = year // 100 + (year % 100 > 0)
    print(cent)
    return 0
def main():
    """Main Function"""
    time = int(input())
    for _ in range(time):
        check(input())

main()
