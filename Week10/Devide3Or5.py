"""Divide3Or5"""
def main():
    """Main"""
    ans = 0
    loop = int(input())
    for i in range(loop+1):
        if i % 3 == 0 or i % 5 == 0:
            ans += i
    print(ans)

main()
