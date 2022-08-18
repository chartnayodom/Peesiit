"""[Midterm] LargestNumber"""
def find(num1, num2):
    """main function"""
    if num1 > num2:
        return num1
    return num2
def main():
    """main Function"""
    num_1 = input()
    num_2 = input()
    num_3 = input()
    last = num_1 + num_2 + num_3
    last = find((num_1 + num_3 + num_2), last)
    last = find((num_2 + num_1 + num_3), last)
    last = find((num_2 + num_3 + num_1), last)
    last = find((num_3 + num_2 + num_1), last)
    last = find((num_3 + num_1 + num_2), last)
    print(int(last))
main()
