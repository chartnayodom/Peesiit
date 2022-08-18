"""ATM"""
def main():
    money = int(input())
    balance = money
    working = True
    while working:
        cmd = input().split()
        # print(cmd)
        if cmd[0] == "D":
            balance += int(cmd[1])
        elif cmd[0] == "W":
            if int(cmd[1]) > balance:
                balance = 0
            else:
                balance -= int(cmd[1])
        elif cmd[0] == "END":
            working = False
    print(balance)
main()
