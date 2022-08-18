"""FizzBuzz"""
def main():
    """Main Function"""
    num = int(input())
    for chk in range(1, num+1):
        if chk % 3 == 0 and chk % 5 == 0:
            print("FizzBuzz")
        elif chk % 5 == 0:
            print("Buzz")
        elif chk % 3 == 0:
            print("Fizz")
        else:
            print(chk)
main()
