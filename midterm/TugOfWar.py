"""TugOfWar"""
def main():
    """Main Function"""
    pow_a = 0
    pow_b = 0
    for _ in range(10):
        pow_a += int(input())
    for _ in range(10):
        pow_b += int(input())
    if pow_a > pow_b:
        print('B')
    if pow_a < pow_b:
        print('A')
    if pow_a == pow_b:
        print('AB')
main()
