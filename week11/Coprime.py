"""CoprimeV1"""
def main():
    num1 = int(input())
    num2 = int(input())
    if num1 >= num2:
        loop = num1
    else:
        loop = num2
    ans = 0
    for i in range(1, loop, 1):
        if num1 % i == 0 and num2 % i == 0:
            ans = i
        # else:
        #     ans = i
    print(ans)
main()