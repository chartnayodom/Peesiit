"""GCD_V1"""
def main():
    """main"""
    num_1 = abs(int(input()))
    num_2 = abs(int(input()))
    loop = 1
    ans = 0
    if num_1 == 0:
        num_1 = num_2
    elif num_2 == 0:
        num_2 = num_1
    while True:
        if num_1 % loop == 0 and num_2 % loop == 0:
            ans = loop
        if loop == num_1 or loop == num_2:
            break
        else:
            pass
        loop += 1
    print(ans)
main()
