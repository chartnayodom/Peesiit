"""[Midterm] Harshad"""
def main():
    """Main Function"""
    for _ in range(10):
        num = abs(int(input()))
        if num == 0:
            print("No")
            continue
        else:
            pass
        num2 = str(num)
        check = 0
        for i in num2:
            check += int(i)
        #print(check)
        if num % check:
            print("No")
        else:
            print("Yes")

main()
