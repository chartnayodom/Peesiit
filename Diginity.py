"""DIginity"""
def digit(number):
    """digit"""
    num_check = number
    while True:
        if len(num_check) <= 1:
            print(num_check)
            break
        else:
            sum_1 = 0
            for i in num_check:
                sum_1 += int(i)
            num_check = str(sum_1)
    #print(ans)
def main():
    """Main function"""
    #number = 0
    while True:
        inp_num = int(input())
        if inp_num == 0:
            break
        else:
            digit(str(inp_num))
    # for i in number:
    #     sum_1 = 0
    #     sum_1 += i
    #     ans = sum_1 % 10
    # print(ans)
main()
