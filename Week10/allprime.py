"""allprime"""
def prime(num):
    """find prime number"""
    if num <= 1:
        # print("No")
        return 0
    for i in range(2, num):
        if num % i == 0:
            # print("No")
            return 0
    return 1

def main():
    """main"""
    num = int(input())
    count = 0
    for i in range(1, num+1):
        count += prime(i)
    print(count)
main()
