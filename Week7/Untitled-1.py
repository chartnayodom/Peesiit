"""Sequence XII"""
def main():
    """Main function"""
    number = int(input())
    k_1 = number*2-1
    ans = number
    anss = 0
    for i in range(k_1):
        for j in range(k_1):
            if i == j or i+j == k_1-1:
                ans = number
                anss = 0
                print('%02d'%ans, end=" ")
            elif j == number-1 and i < number:
                ans = i+1
                anss = number
                print('%02d'%ans, end=" ")
            elif j == number-1 and i >= number:
                ans = k_1-i
                anss = number
                print('%02d'%ans, end=" ")
            elif j == 0 and i >= number:
                ans = i-number+2
                anss = number
                print('%02d'%ans, end=" ")
            elif j == k_1-1 and i < number or j == 0 and i < number:
                ans = number-i
                anss = number
                print('%02d'%ans, end=" ")
            else:
                print('%02d'%ans, end=" ")
            if anss >= 1:
                ans += 1
                anss += -1
            elif ans == 1:
                ans += 1
                anss = 10
            else:
                ans += -1
        print()
main()
