"""[Midterm] One For All"""
def main():
    """Main Function"""
    num = int(input())
    name = ''
    for i in range(1, num+1):
        nam = input()
        name += nam
        if i % 2 == 0 and i != num:
            name += '-' * i
        elif i == num:
            name += '_'
            name += str(num)
        else:
            name += '*' * i
    print(name)
main()
